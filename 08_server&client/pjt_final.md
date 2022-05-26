- 하위 컴포넌트 참조

```python
from ..movies.models import Movie
'ImportError: attempted relative import beyond top-level package'
=> 해결
movies가 settings의 installapp에 들어있기 때문에, 상대경로를 안쓰더라도
movies에서 바로 사용할 수 있다.
from movies.models import Movie
from movies.serializers import MovieSerializer
```



- [날짜 관련 패키지 설치](https://erim1005.tistory.com/entry/vue-moment-%EC%A0%81%EC%9A%A9-%EB%B0%8F-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95)

```js
$ npm install vue-moment --save

import Vue from 'vue'
import vueMoment from 'vue-moment'
Vue.use(vueMoment)

Vue.$moment 로 호출하여 사용할 수 있다. 
스크립트에서는 this.$moment 를 사용하고 template markup 에서는 {{$moment}}를 사용
```



- object는 비어있어도, v-if시 true로 인식되서 lodash로 isEmpty 검사

```vue
<p>LIKE Movie:
<span v-if="ifNotGenre">영화를 좋아요하러 가보세요 !</span>
    
<script>
  computed:{
    ...mapGetters(['profile',]),       
    likeGenres(){
      return this.profile.like_movies
    },
    ifNotGenre(){
      if(_.isEmpty(this.likeGenres)){
        return true}
      else{  return false  }}},
</script>
```



- profileView.vue

```vue
ProfileView.vue
--- ProfileArticleList.vue
```

프로필에서,  프로필 데이터를 로드할때 
내가 쓴 게시물이 재접속해야만 로드가 되고, 처음 페이지 접속 시 로드 되지 않았음.
`store/modules/accounts.js`에서 `isProfile: state => !_.isEmpty(state.profile)`를 설정해주었다.

이를 하위 컴포넌트인, `ProfileArticleList.vue`에서 프로필이 있을때 바로 로드되도록 `v-if`를 설정해주었다.

```vue
<div v-if="isProfile" class="row">
      <article-item
        v-for="article in articles"
        :key="article.pk"
        :article="article"></article-item>	
```



- signup과정에서, 사진파일을 업로드할때 data를 object에 담지않고, formdata에 담아서 보내야함.
  또한 사진은 v-model을 사용하지 않는다

  [참고]([https://velog.io/@ready2start/DRF-djrestauth%EB%A1%9C-%EC%BB%A4%EC%8A%A4%ED%85%80-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0](https://velog.io/@ready2start/DRF-djrestauth로-커스텀-회원가입-구현하기))

```js
methds:{
    newFormdata(){
        const formdata = new Formdata()
    }
}
```
