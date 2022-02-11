# PJT 03

#### 이번 pjt를 통해 배운 내용

- html, css, bootstrap을 이용하여 반응형 웹페이지 만들기



#### A. nav_footer

- 요구사항: navbar에 아이콘 삽입, 토글 이용해보기, 모달에 로그인창 넣기 
- 코드

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">

  <title>Navbar Footer Test</title>
</head>
<body>
  <!-- 01_nav_footer.html -->
  <nav class="navbar navbar-dark bg-dark sticky-top navbar-expand-md">
    <div class="container-fluid">
      <a href="02_home.html"><img src="images/logo.png" alt="images" width="100px"></a>
      <div>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
          <ul class="navbar-nav">
            <li><a class="nav-link active" aria-current="page" href="02_home.html">Home</a></li>
            <li><a class="nav-link" href="03_community.html">Community</a></li>
            <li><a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal" >Login</a></li>
          </ul>
      </div>
      </div>
    </div>
  </nav>
  
  
<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
          </div>
          <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Check me out</label>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
  <footer class="d-flex align-items-end justify-content-center my-5">
    박다빈
  </footer>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
</body>
</html>
```

- 어려웠던 점

  ​	bootstrap이 익숙하지 않아서 계속 문제에서 요구하는 것과 다른 코드를 가져와서 오래걸렸다.

  ​	요소를 잘 묶어주지 않아서 justify-content부분이 실행이 되지 않았다.

- 문제의 포인트

  ```html
   <ul class="navbar-nav">
   	<li><a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal" >Login</a></li>  
       #data-bs-toggle="modal" 을 넣어서 연결시켜준다. data-bs-target="#exampleModal" target과
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      #id="exampleModal" id가 갖는 값이 일치해야 한다.
  ```

  

#### B. home

- 요구사항: carousel 사용해보기, 카드를 이용하여 home에 해당하는 이미지 card로 넣기!
  - Section 내부의 요소(article)들은 Viewport의 가로 크기가 576px미만일 경우에는 한 행 (row)에 1개씩 표시됩니다. 
  -  Section 내부의 요소(article)들은 Viewport의 가로 크기가 576px이상일 경우에는 한 행 (row)에 2개 이상 자유롭게 표시합니다. 

- 코드

```html
  <header class="container" >
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/header1.jpg" class="d-block w-100" alt="img">
        </div>
        <div class="carousel-item">
          <img src="images/header2.jpg" class="d-block w-100" alt="img">
        </div>
        <div class="carousel-item">
          <img src="images/header3.jpg" class="d-block w-100" alt="img">
        </div>
      </div>
    </div>
  </header>

  <h1 class="boxoffice">Boxoffice</h1>

  <section>
    <div class="carsection d-flex justify-content-center row row-cols-1 row-cols-md-2 g-4">
      <div class="col">
        <div class="card">
          <img src="images/movie1.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie2.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie3.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie4.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie5.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie6.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>

    </div>
  </section>
```

```css
/* 02_home.css */
.boxoffice{
display: flex;
justify-content: center;
margin: 1rem;
font-weight: bolder;
}

.col{
  width: 500px;
}
```

- 어려웠던 점

  ​	이전에 많이 실습했던 부분이여서 쉽게 할 수 있었던 것 같다!

  ​	

- 문제의 포인트

  carousel 사용해보기, 카드를 이용하여 home에 해당하는 이미지 card로 넣기!

#### C. community

- 요구사항: community를  강조합니다. (active) 

  - 게시판 목록과 게시판은 div.main 요소로 둘러 쌓여 있습니다. 
  -  게시판 목록은 aside 요소, 목록 내부의 각 항목(Boxoffice, Movies, Genres, Actors)은 List group  컴포넌트
  - Viewport의 가로 크기가 992px 이상일 경우에는 게시판 목록 내부의 항목 (Boxoffice, Movies, Genres, Actors)은 div.main영역의 내부에서 좌측 1/6 만큼 의 너비를 가집니다. 
  - Viewport의 가로 크기가 992px 미만일 경우에는 게시판 목록 내부의 항목 (Boxoffice, Movies, Genres, Actors)은 div.main영역의 내부에서 전체만큼의 너 비를 가집니다. 

  - 게시판은 Viewport의 가로크기에 따라 전혀 다른 요소를 표시합니다. 
    -  A. Viewport의 가로 크기가 992px 이상일 경우에는 게시글이 표(table) 요소로  표시되며, div.main영역의 내부에서 우측 5/6 만큼의 너비를 가집니다.  
    - B. Viewport의 가로 크기가 992px 미만일 경우에는 게시글이 글(article) 요소들 의 집합으로 표시되고 가로선으로 구분합니다(스타일링은 자유롭게 진행합니 다). div.main영역의 내부에서 전체만큼의 너비를 가집니다. 
  - 게시글 페이징(paginator)은 게시판 아래에 위치

- 코드

```html
  <div class="main">
    <h1 class="d-flex justify-content-center">Community</h1>
    
    <!-- Sidebar -->
    <!-- lg 이상: 좌측 1/6 너비 가짐 -->
    <!-- lg 미만: 전체의 너비 가짐 -->
    <!-- 요소 반응형으로 묶어주기 -->
    <div class="row">
      <aside class="list-group col-12 col-md-2">
        <ul class="list-group_ul container">
          <li><a class="list-group-item" href="#">Boxoffice</a></li>
          <li><a class="list-group-item" href="#">Movies</a></li>
          <li><a class="list-group-item" href="#">Genres</a></li>
          <li><a class="list-group-item" href="#">Actor</a></li>
        </ul>
      </aside>

    <!-- Board -->
      <section class="col-12 col-md-10">
        <div class="d-none d-md-block">
          <!-- 커질때 보임 -->
          <table class="table table-striped container">
            <thead>
              <tr>
                <th scope="col">영화제목</th>
                <th scope="col">글 제목</th>
                <th scope="col">작성자</th>
                <th scope="col">작성 시간</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td colspan="2">Larry the Bird</td>
                <td>@twitter</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

        <div class="d-md-none">
          <!-- lg이상에서 안보임 -->
          <article>
            <ul class="list-group list-group-flush container">
              <li class="list-group-item">An item</li>
              <li class="list-group-item">A second item</li>
              <li class="list-group-item">A third item</li>
              <li class="list-group-item">A fourth item</li>
              <li class="list-group-item">And a fifth one</li>
            </ul>
          </article>
          <!-- table low -->
          <nav aria-label="paginator">
            <ul class="pagination d-flex justify-content-center">
              <li class="page-item disabled">
                <a class="page-link">Previous</a>
              </li>
              <li class="page-item"><a class="page-link" href="#">1</a></li>
              <li class="page-item active" aria-current="page">
                <a class="page-link" href="#">2</a>
              </li>
              <li class="page-item"><a class="page-link" href="#">3</a></li>
              <li class="page-item">
                <a class="page-link" href="#">Next</a>
              </li>
            </ul>
          </nav>
        </div>
      </section>
  </div>
```

```css
/* 03_community.css */
.list-group_ul{
  list-style-type: none;
}

/* .sticky{
  position: -webkit-sticky;
  position: sticky;
} */
```

- 어려웠던 점

  ​	많은 요소들의 너비를 지정해야해서 어려웠다.

- 문제의 포인트

  문제에서 요구하는 Viewport의 크기를 맞추는 것이 중요하다고 생각되었다.

  - lg이상일때 보이는 sidebar, 게시판

  - lg 미만일때 보이는 sidebar, (사이즈와 양식이) 변경된 게시판, paginator 

​	

#### 후기

커뮤니티의 변경된 게시판 목록을 만드는 것에 있어 lg보다 클때의 게시판의 양식을 연결하는 방법을 알지 못해 완성하지 못했다. 그 외 웹 페이지를 완성하고 동작이 되서 신기했다. 카드를 가져온 부분은 익숙해서 빠르게 할 수 있었지만, 처음 해보는 부분들을 할 땐 조금 막막했던 것 같다. 하나의 웹페이지를 완성해서 뿌듯하다!