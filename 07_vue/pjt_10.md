# pjt10. Vue를 활용한 SPA 구성

### 컴포넌트 구성

- 명세서에 주어진 대로, 6개의 컴포넌트를 생성했다.

- 또한, 각각 알맞게 vue를 상속해주었다.

```vue
<template>
  <div>
    <b-card
      :img-src="movie.poster_path"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
    >
      <b-card-text class="title">
        {{ movie.title }}
      </b-card-text>
      <b-card-text class="overview">
        {{ movie.overview }}
      </b-card-text>
    </b-card>
  </div>
```





### router와 vuex 사용

- `vue add router`와 `vue add vuex`를 통해 router와 vuex를 사용할 기본 환경을 생성해주었다.
- router
  - 알맞은 path와 component를 연결시켜주었다.

```js
// router/index.js

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/random',
    name: 'random',
    component: RandomView
  },
  {
    path: '/watch-list',
    name: 'watch-list',
    component: WatchListView
  },
]
```

- vuex
  - 사용할 data인 movies, randomMovie, watchList를 state에 만들어 주었다.
  - 위 state를 조작하는 mutations를 세 개 만들었다.
  - 처음 페이지가 로딩되었을 때 axios요청을 통해 movies 리스트를 가져오는 loadMovies와 랜덤으로 영화를 골라주는 pickMovie, WatchListForm에서 입력된 영화제목을 저장할 watchMovie actions를 생성해주었다.

```js
  state: {
    movies:[],
    randomMovie: null,
    watchList:[]
  }, 
  mutations: {
    LOAD_MOVIES (state, movies) {
      state.movies = movies
    },
    PICK_MOVIE (state) {
      state.randomMovie = _.sample(state.movies)
    },
    WATCH_MOVIE(state, watchItem){
      state.watchList.push(watchItem)
      // console.log(JSON.stringify(watchItem))
    }
  },
  actions: {
    loadMovies (context) {
      const params ={
        api_key: API_KEY,
        language : 'ko',
        region : 'KR'
      }
      const movies = []
      axios({
        method: 'get',
        url: API_URL,
        params
      })
      .then(res=>{
        res.data.results.forEach((movie)=>{
          movies.push({
            title : movie.title,
            overview : movie.overview,
            poster_path:'https://image.tmdb.org/t/p/w500'+movie.poster_path
          })
        })
      })
      context.commit('LOAD_MOVIES', movies)
    },
    pickMovie (context) {
      context.commit('PICK_MOVIE')
    },
    watchMovie(context, watchItem){
      context.commit('WATCH_MOVIE', watchItem)
    }
  },
```

- action에서 axios요청으로 movie에 필요한것들을 movies에 push 해주었다.



### App.vue

- 네비게이션 바에 router-link를 위치시켰고, 네비게이션 바 바로 하단에 router-view를 위치시켰다.

```vue
<template>
  <div id="app" >
    <b-navbar type="dark" class="d-flex justify-content-between sticky-top">
      <b-navbar-brand href="/"><img src="./assets/ssafy-logo.png" alt="logo" class="logo"></b-navbar-brand>
      <b-navbar-nav>
        <router-link to="/">Home</router-link>
        <router-link to="/random">Random</router-link>
        <router-link to="/watch-list">MyMovieList</router-link>
      </b-navbar-nav>
    </b-navbar>
    <router-view/>
  </div>
</template>
```

- script부분은 App이 생성되었을 때 movies를 받아오기 위한 axios요청을 보내는 created를 만들어주었다.

```vue
<script>
export default {
  name:'App',
  created () {
    this.$store.dispatch('loadMovies')
  }
}
</script>
```



### HomeView.vue

- v-for를 통해 MovieCard를 여러번 불러오는 식으로 구성했다. 이를 위해 store의 movies state를 mapState를 통해 computed에 불러와줬다.

```vue
<template>
  <div class="container">
    <div class="row">
      <movie-card
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        class="cards col-4"
      ></movie-card>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'HomeView',
  components: {
    MovieCard,
  },
  computed: {
    ...mapState(['movies',])
  }
}
</script>
```



### MovieCard.vue

- 부트스트랩의 b-card를 통해 카드모양으로 구성했으며, HomeView에서 넘겨받은 props를 통해 데이터를 넣어줬다.
- 또한 overview가 과도하게 길 때, 4줄만 표시되도록 하기위해 display에 webkit-box 속성을 주었다.

```vue
<template>
  <div>
    <b-card
      :img-src="movie.poster_path"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
    >
      <b-card-text class="title">
        {{ movie.title }}
      </b-card-text>
      <b-card-text class="overview">
        {{ movie.overview }}
      </b-card-text>
    </b-card>
  </div>    
</template>

<script>
export default {
  name:"MovieCard",

  props: {
    movie: Object,
  }
}
</script>

<style>
.title {
  font-weight: bold;
  font-size: 20px;
}

.overview {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
</style>
```



### RandomView.vue

- movies state에서 무작위로 영화 하나를 가져오기 위해 버튼에 pickMovie action을 연결시켜주었다.

```vue
<template>
  <div>
    <b-button variant="success" class="pick-button my-3"
      @click="pickMovie"
    >PICK</b-button>

    <movie-card class="d-flex justify-content-center"
      :movie="randomMovie"
    ></movie-card>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import MovieCard from './MovieCard.vue'

export default {
  components: { MovieCard },
  name: 'RandomView',
  computed: {
    ...mapState(['randomMovie',])
  },
  methods: {
    ...mapActions(['pickMovie',])
  }
}
</script>

<style>
button.pick-button {
  width: 300px;
}
</style>
```

### watchlist

```vue
<template>
  <div>
    <watch-list-form></watch-list-form>
    <watch-list-item 
    v-for="(watch, idx) in watchList"
    :key="watch.date"
    :watch="watch"
    :idx="idx"
    ></watch-list-item>
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem.vue'
import WatchListForm from '@/components/WatchListForm.vue'
import { mapState } from 'vuex'
export default {
  name:'WatchListView',
  components:{
    WatchListItem,WatchListForm
  },
  computed:{
    ...mapState(['watchList',])
  },
}
</script>
```

- idx를 꺼내서, bg-color를 구분해주었다.

```vue
<template>
  <div  class="d-flex justify-content-center">
    <p class="watchlist my-0" :class="{'grey':isTrue, 'greywhite':!isTrue}">{{watch.title}}</p>
  </div>
</template>

<script>
export default {
  name:'WatchListItem',
  props:{
    watch:Object,
    idx:Number
  },
  computed:{
    isTrue(){
      if(this.idx%2){
        return true
      }else{
        return false
      }}}}</script>
<style>
.grey{
  background-color: #e2f1fc;
}
.greywhite{
  background-color: #b0bec9;
}</style>
```

```js
export default new Vuex.Store({
    state: {
        watchList:[]
    },
    mutations: {
    WATCH_MOVIE(state, watchItem){
      state.watchList.push(watchItem)
      // console.log(JSON.stringify(watchItem))
    },},
  actions: {
    watchMovie(context, watchItem){
      context.commit('WATCH_MOVIE', watchItem)
    }  } 
```


