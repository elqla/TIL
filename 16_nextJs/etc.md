

- 넥스트는 getStaticProps를 사용하지 않아도 기본적으로 프리렌더링이 되는건가요?

  - yes

  - ssg면 빌드타임에 프리렌더링


  ssr하면 런타임에 프리렌더링

  둘다안쓰면  ssg

  빌드 치면 어떤페이지들이 ssr 인지 ssg 인지 터미널에 뜸



- https://ko.reactjs.org/docs/higher-order-components.html

- 컨텍스트 프로바이더처럼 

  필요한 페이지마다 헤더를 감싸주면됨

  ```jsx
  export default withHeader(PageComponent)
  또는
  const withHeader = Component = () => {
    return <Header><Compoent/></Header>
  }
  ```

- 페이지마다 임포트해서 위에다 써줄필요도없고 묶어서 withHeader라는 함수에 컴포넌트만 넣어주면 됨
