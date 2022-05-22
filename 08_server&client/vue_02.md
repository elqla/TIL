# Vue router

- components: 부품
- views: url과 mapping될 컴포넌트: router.index.js에 쓰임

```js
import LoginView from '@/views/LoginView.vue'
{
    path:'/login',
    name:'login',
    component: LoginView
}
```



### 404 page

1. vue router에 등록되지 않은 routes일 경우 `/no-such-routes`

```js
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',  //마지막에쓰기
    redirect: '/404'   //redirect
  },
```

2. vuerouter에 등록되어 있지만, 서버에서 해당 리소스를 찾을 수 없는 경우 `/articles/123455`

- ![image-20220518095155919](images/image-20220518095155919.png).

  

### Navigation Guard

- 전역가드
  - URL을 이동할때마다, 이동하기 전 모든 경우 발생
  - login required같은

![image-20220518101941723](images/image-20220518101941723.png).

```js
router.beforeEach((to, from, next) =>{
    //로그인 여부 확인(vuex 사용시)
    const {isLoggedIn} = store.getters
    //auth가 필요한 router의 name
    const authPages = ['articleNew', 'articleEdit']
    //현재 이동하고자 하는 페이지가 auth가 필요한가 ?
    const isAuthRequired = authPages.includes(to.name) //가려고 하는 to.name 이 있는지
    //auth가 필요한데, 로그인 되어있지 않다면 ?
    if (isAuthRequired&&!isLoggedIn){
        //로그인 페이지로 이동
        next({name:'login'})
    }else{
        //원래 이동하려던 곳
        next()
    }
})
```



# Vuex

### Vuex modules & namespace

<img src="images/image-20220521180324428.png" alt="image-20220521180324428" style="zoom:50%;" />. 

vuex는 store/index.js에 사용하지만, App이 커질수록 파일이 커지므로 modules 폴더를 만들어 분리해준다.

![image-20220521180718383](images/image-20220521180718383.png)

- 모듈별 분리: namespaced: true 적용

  ```js
  const store = createStore({
    modules: {
      account: {namespaced: true}
    }  //혹은 아래처럼
  ```



## accounts

```js
export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},  //현재 사용자
    profile: {},  //누구 프로필 ?
    authError: null,
  },
```

- state 작성 후, mutation 작성

```js
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error
  },
```

- getters : state를 getter통해 접근

```js
  getters: {
    isLoggedIn: state => !!state.token, //유효한 토큰이 있으면 로그인한것임. T/F want
    currentUser: state => state.currentUser,  // state => {return state.currentUser}
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`})
  },
```

- actions

```js
  actions: {
    saveToken({ commit }, token) {
      /* 
      state.token 추가 
      localStorage에 token 추가
      로그인, 회원가입 시
      */
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)  //key, value
    },

    removeToken({ commit }) {
      /* 
      state.token 삭제
      localStorage에 token 추가
      */
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    login({ commit, dispatch }, credentials) {
      /* 
      POST: 사용자 입력정보를 login URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'articles' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    signup({ commit, dispatch }, credentials) {
      /*      
      POST: 사용자 입력정보를 signup URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials  // credentials = 사용자 입력 정보
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'articles' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    logout({ getters, dispatch }) {
      /* 
      POST: token을 logout URL로 보내기
        성공하면
          토큰 삭제
          사용자 알람
          LoginView로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        // data: {},
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          alert('성공적으로 logout!')
          router.push({ name: 'login' })
        })
        .error(err => {
          console.error(err.response)
        })
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      /*
      GET: 사용자가 로그인 했다면(토큰이 있다면)
        currentUserInfo URL로 요청보내기
          성공하면
            state.cuurentUser에 저장
          실패하면(토큰이 잘못되었다면)
            기존 토큰 삭제
            LoginView로 이동
      */
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_CURRENT_USER', res.data))
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchProfile({ commit, getters }, { username }) {
      /*
      GET: profile URL로 요청보내기
        성공하면
          state.profile에 저장
      */
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
    },
  },
}

```











- django-> API       데이터 건네줌

vue -> JS     axios요청 보내서(django한테)

```
# view파일 생성 + router에 등록 + app.vue(<router-link to='/articles'>article) + store에서 기능 만들기

+ article.vue만들기
articles먼저 만들기, 장고에서 정보 가져와서 actions에서 console.log찍어보기, ->article.title

로그인 해주기

```



```js
isAuthRequired : 인증 필요 여부
isLoggedIn: 로그인 여부
## 인증이 필요한데, 로그인 안된경우 로그인하러 가야함

//router
beforeEAch(()=>{
	const isAuthRequired = authPages.includes(to.name)// boolean t -> 인증 need
})
```



```
optional chaning 
article = {user:'다빈'}
article.user?.username
article?.user.username // 없으면 에러뜨는데, 방지하기 위함  // undefined로 출력됨
```





```
state.모듈.변수
모듈 안에 state니까 모듈.state겠지 하는데 아님

getrers
state.article.articles
getters.articles로 바로 접근 가능 // 변수명 겹치지 않도록....!

getters를 computed로만 쓰거나/ 재정의 하는 부분으로 쓰거나
```





axios 러닝 가이드



인터셉터



