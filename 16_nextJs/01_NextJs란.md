## The React Framework for Production

### A FullStack Framework for ReactJs

1. **서버사이드 렌더링**

   - SEO 최적화, DataFetching 용이

   - 서버 측에서 React Page, Components를 미리 렌더링 해줌

   - nextJs has built in SSR (use Node.js)

   - **리액트**

     1. CSR(클라이언트 사이드 렌더링)으로 서버가 아닌, 사용자의 브라우저에서 처리가 됨

     2. 클라이언트 측 JScode가 실행된 후 DataFetching됨
        - 이때, 전송된 요청의 회신을 대기하며 로딩이 생김 (요청된 페이지가 아직 해당 데이터를 포함하지 않음)

     3. SEO(검색엔진 최적화): 로그인해야 볼 수 있는 부분의 경우, SEO가 중요하지 않다.

        - 대부분의 페이지는 SEO가 중요하다.

        - 그러나 CSR은 검색 시 서버가 빈 HTML문서를 가져오기 때문에 SEO최적화가 불가능하다.

          -> 서버사이드 렌더링

2. **파일기반의 라우트**
   - File-Based Routing
   - Define pages and routes with files and folders instead of code
     - React는 라우터가 없음 (다른 컴포넌트를 보여줌) - SPA(싱글페이지애플리케이션)
   - :star: pages라고 설정해야만 하는 폴더가 존재
     - Route와 Path를 정의하는 폴더를 구조화하게됨

3. **풀스택 능력**



## SETUP

```
npx create-next-app
```


