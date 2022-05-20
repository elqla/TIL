- components: 부품
- views: url과 mapping



router_index.js

# Vue router

### 404 page

vue router에 등록되지 않은 routes일 경우 `/no-such-routes`

vuerouter에 등록되어 있지만, 서버에서 해당 리소스를 찾을 수 없는 경우 `/articles/123455`

```js
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
```

- 서버에서 해당 리소스를 찾을 수 없는 경우

- ![image-20220518095155919](images/image-20220518095155919.png).

  

### Navigation Guard

- 전역가드
  - URL을 이동할때마다, 이동하기 전 모든 경우 발생

![image-20220518101941723](images/image-20220518101941723.png).

# Vuex

### Vuex modules & namespace





django-> API       데이터 건네줌

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



