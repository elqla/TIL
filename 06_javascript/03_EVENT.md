## dom 조작 실습

- Event
  - 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
  - 이벤트 발생
    - UI event
      - 마우스 클릭, 키보드, INPUT, FOCUS
    - `Element.click()`
  - `~하면, ~한다.`

### event handler

- `EventTarget.addListener()`
  - 지정한 이벤트가 대상에 전달될때마다, 호출할 함수를 설정
- `target.addEventLister(type, listener [, options])`
  - `target.addEventLister(동작, 함수)`
  - `type`
    - 반응할 이벤트 유형
  - `listener` ---`recipe`
    - 지정된 타입의 이벤트가 발생했을때, 알림을 받는 객체
    - eventlistner인터페이스 혹은 JS function 객체(콜백함수)여야 함

```html
<body>
  <!-- 1. onclick -->
  <button onclick="alertMessage()">나를 눌러봐!</button>  <!--inline으로 ()쓰지말고 뒤에 걸기 ㄱ -->

  <!-- 2-1. addEventListener -->
  <button id="my-button">나를 눌러봐2!!</button>
  <hr>

	<!-- 2-2. addEventListener -->
  <p id="my-paragraph"></p>

  <form action="#">
    <label for="my-text-input">내용을 입력하세요.</label>
    <input id="my-text-input" type="text">
  </form>
  <hr>

  <!-- 2-3. addEventListener -->
  <h2>Change My Color</h2>
  <label for="change-color-input">원하는 색상을 영어로 입력하세요.</label>
  <input id="change-color-input"></input>
  <hr>

  <script>
    // 1 나를 눌러봐 2
    const alertMessage = function () {  //event 안되도 되지만 _ !
      alert('메롱!!!')
    }

    const arr = [1, 2, 3]

    // 2-1
    const myButton = document.querySelector('#my-button')
    myButton.addEventListener('click', alertMessage)  
    <!-- alertMessage()를 쓰면 return 값이 없어서 undefined랑 동일  //  내가 실행한게 아님 !  click이 발생할때 실행-->

    // 2-2
    const myTextInput = document.querySelector('#my-text-input')
    const myP = document.querySelector('#my-paragraph')
    
    myTextInput.addEventListener('input', function (event) { //익명함수(함수를 이름없이 넣기 =>)
      // console.log(event.target.value)   //event.target = event가 발생한 대상
      myP.innerText = event.target.value   //this가 없기 때문에 arrow를 써도됨 ?
    })

    // Arrow Function Refactoring 한다면?
    // myTextInput.addEventListener('input', event => myP.innerText = event.target.value)

    

    // 2-3
    const h2Tag = document.querySelector('h2')

    const onColorInput = function (event) {
      const userInput = event.target.value
      h2Tag.style.color = userInput
    }

    const colorInput = document.querySelector('#change-color-input')
    colorInput.addEventListener('input', onColorInput)
      // 
  </script>
</body>
</html>
```



```js
    myButton.addEventListener('click', alertMessage())
===  myButton.addEventListener('click', undefined) // return 이 없음
// 또한, 함수명세를 넣어놓고, 클릭이 넣을때까지 대기_____클릭이 일어나면 함수 실행
// ()를 쓰는건 실행된 함수의 값(결과)를 넣어놓고 기다리는 것
```



- 이벤트 취소

- `event.preventDefault()`
  - 현재 이벤트의 기본 동작을 중단
  
  - HTML요소의 기본 동작을 작동하지 않게 막음
  
  - 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소
  
    

1. 입력을 받아 form을 만들어
2. submit 동작 -> 이벤트 트리거가 되라

- `stopPropagation` 이 존재한다.

---

참고

콜백(Callback)이란 옵저버(Observer) 디자인 패턴에서 나온 개념으로 객체의 상태 변화(이벤트)가 발생하였을 경우에 이러한 사실을 함수를 통해 전달하게 되는데, 이를 콜백 함수라고 합니다.

https://beomy.tistory.com/10?category=591557 [beomy]