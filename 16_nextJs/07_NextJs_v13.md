## Route

- App directory

[Img](https://nextjs.org/_next/image?url%3D%2Fdocs%2Flight%2Fproject-organization-private-folders.png%26w%3D3840%26q%3D75%26dpl%3Ddpl_5PwFtC7dn1cJkeJ8CTR2vPDLubXw)

`app` folder 하위에

`pages.js` 혹은 `route.js`로 끝날 경우 Routable 하다.

`layout.js > templates.js`

```js
app/pages.js -> routable
app/dashboard/route.js -> routable
```

그렇다면 app directory 안에 components나 style같은 폴더도 routable해질수 있다는 것
-> 따라서 이는 private folder라고 하여 `_folderName`으로 폴더명을 만들어 사용할 수 있다.

<img src="./images/2023-09-12%20%EC%98%A4%ED%9B%84%202.25.14.png" >

## Route Group

`(folderName)` 으로 정의하면 그룹화해서 routing 할 수 있다.

### Rules

- 파일, 폴더이름이 곧 url => camelCase 쓰지않기

### getStaticParams

[문서읽기](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes#generating-static-params)

```tsx
export async function generateStaticParams() {
  const posts = await fetch("https://.../posts").then((res) => res.json());

  return posts.map((post) => ({
    slug: post.slug,
  }));
}
```

Request Memoization

- React는 fetchAPI를 확장하여 동일한 URL과 옵션을 가진 요청을 자동으로 메모합니다 . 이는 React 컴포넌트 트리의 여러 위치에서 동일한 데이터에 대한 가져오기 함수를 한 번만 실행하면서 호출할 수 있음을 의미합니다.

  -> 즉 여러 곳에서 호출할때, 데이터를 저장하고 사용하지 않아도 됨. API호출을 하고, 같은 정보를 return 한다.

```ts
async function getItem() {
  // The `fetch` function is automatically memoized and the result
  // is cached
  const res = await fetch("https://.../item/1");
  return res.json();
}

// This function is called twice, but only executed the first time
const item = await getItem(); // cache MISS

// The second call could be anywhere in your route
const item = await getItem(); // cache HIT
```

## Parallel Routes \_ 병렬 라우팅

<img src="./images/2023-09-13 오후 2.24.11.png"/>

```tsx
import { getUser } from "@/lib/auth";
export default function Layout({ dashboard, login }) {
  const isLoggedIn = getUser();
  return isLoggedIn ? dashboard : login;
}
```

## Route Handlers

https://nextjs.org/docs/app/building-your-application/routing/route-handlers

읽어보기 !!

## Data Fetching

https://nextjs.org/docs/app/building-your-application/data-fetching
