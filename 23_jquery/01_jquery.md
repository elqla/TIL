[TOC]

# Wrapper

- jQuery (element object | css style selector)라고 시작되는 함수

**Wrapper의 안전한 사용**

- $(element)와 jquery(element)는 같은의미지만, $를 사용하는 타 라이브러리와 충돌이 있을수 있다.

```html
<script>
  (function ($) {
    // jquery code here
    // 우선순위 : local 변수 > global 변수
    $("body").html("hello world");
  })(jQuery);
  // -> 선언 + 호출
</script>
```

**제어 대상을 지정하는 방법**

- jQuery(selector, [context(option)])
- jQuery(element)

ex) jQuery(selector, [context])

```html
<script type="text/javascript">
  (function ($) {
    $("ul.foo").click(function () {
      $("li", this).css("background-color", "red");
    });
  })(jQuery);
</script>
```

ex) jQuery(element)

```html
<script type="text/javascript">
  jQuery(document.body).css("background-color", black);
</script>
```

# Selector

- css selector 를 많이 씀 : 효과적인 element 선택

[공홈](# https://api.jquery.com/category/selectors/attribute-selectors/)

# Chain

- jquery의 method들은 반환값으로 자기 자신을 반환해야한다는 규칙이 있음.
  -> 한번 선택한 대상에 대해 연속적 제어 가능

```html
<body>
  <a id="tutorial" href="http://jquery.com" target="_self">jQuery</a>
  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/query.min.js"></script>
  <script type="text/javascript">
    jQuery('#tutorial'). attr('href', 'http://jquery.org').attr('target'. '_blank').css('color','red');
    // javascript - tutorial.setAttribute
  </script>
</body>
```

```html
<body>
  <ul class="first">
    <li class= "foo"> list item 1 </li>
    <li> list item 2 </li>
    <li class= "bar"> list item 3 </li>
  <ul>
  <ul class="second">
    <li class="foo"> list item 1 </li>
    <li> list item 2 </li>
  <li class= "bar"> list item 3 </li>
  <ul>
  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
  <script type="text/javascript">
  S('ul.first').find('foo').css('background-color', 'red').end().find(" bar').css('background-(color', 'green");
  </script>
</body>
```

# Event

- click, ready, live
- trigger, bind, unbind

**bind, unbind, trigger 이용한 이벤트 설치, 제거, 호출**

```html
<html>
  <head>
    <script type="text/javascript" src="httes://ajax.googleapis.com/ajax/libs/jguerv/1.6.2/jquery.min.js"></script>
    <script type="text/javascript">
      function clickhandler(e){
      alert('thank you');
      }
      // TODO ready mean
      $(document).bind('ready', function(){
      $('#click-me').bind('click', clickHandler);
      ${('#remove_event').bind('click', function(e){
      $('#click-me').unbind('click' , clickHandler);
      });
      $('#trigger_event').bind('click', function(e){
      $('#click_me').trigger('click'):
      })
      }
      })
    </script>
  </head>
  <body>
    <input id="click_me" type="button" value="click me" /> <input id="remove_event" type="button" value="unbind" /> <input id="trigger_event" type="button" value="trigger" />
  </body>
</html>
```

**이벤트 헬퍼**

```html
<html>
  <head>
    <script type="text/javascript" src="httes://ajax.googleapis.com/ajax/libs/jguerv/1.6.2/jquery.min.js"></script>
    <script type="text/javascript">
      function clickhandler(e) {
        alert("thank you");
      }
      $(document).ready(function () {
        $("#click_me").click(clickhandler);
        $("#remove_event").click(function (e) {
          $("#click_me").unbind("click", clickhandler);
        });
        $("#trigger_event").click(function (e) {
          $("#click_me").trigger("click");
        });
      });
    </script>
  </head>
  <body>
    <input id="click_me" type="button" value="click me" /> <input id="remove_event" type="button" value="unbind" /> <input id="trigger_event" type="button" value="trigger" />
  </body>
</html>
```

**live 를 이용한 이벤트 설치**

- event 위임
- 성능상 문제 있을 수 있음
- 권장 x

```html
<html>
  <head>
    <script type="text/javascript" src="httes://ajax.googleapis.com/ajax/libs/jguerv/1.6.2/jquery.min.js"></script>
    <script type="text/javascript">
      function clickhandler(e) {
        alert("thank you");
      }
      $("#click_me").live("click", clickhandler);
      $("#remove_event").live("click", function (e) {
        $("#click_me").die("click", clickhandler);
      });
      $("#trigger_event").live("click", function (e) {
        $("#click_me").trigger("click");
      });
    </script>
  </head>
  <body></body>
</html>
```

# 엘리먼트 제어 (manipulation)

**자식으로 삽입**

- append, appendTo, html, prepend, prependTo, text

`<p><strong></string></p>`

```html
<body>
  <p>i would like to say:</p>
  <script>
    $("p").append("<strong>Hello</strong>");
  </script>
</body>
```

**형제로 삽입**

- after, before, insertAfter, insertBefore

`<p></p>`
`<strong></strong>`

**부모로 감싸기**

- wrap, unwrap, wrapAll, wrapInner

**삭제**

- detach, empty, remove, upwrap

**치환**

- replace, replaceAll

**클래스**

- addClass, hasClass, removeClass, toggleClass

```html
<head>
  <style></style>
</head>
<body>
  <p class="blue">click to toggle</p>
  <p class="blue highlight">click to toggle</p>
  <script>
    $("p").click(function () {
      $(this).toggleClass("highlight");
    });
  </script>
</body>
```

속성제어

- attr, prop, removeAttr, removeProp, val

```html
<body>
  <input type="text" value="something" />
  <p></p>
  <script>
    $("input")
      .keyup(function () {
        var value = $(this).val(); // event의 value값 알아냄
        $("p").text(value);
      })
      .keyup(); // trigger - 초기값 세팅
  </script>
</body>
```

# 폼

```html
<body>
  <p>
    <input type="text" />
    <span></span>
  </p>
  <script>
    $("input")
      .focus(function () {
        $(this).next("span").html("focus");
      })
      .blur(function () {
        $(this).next("span").html("blur");
      })
      .change(function (e) {
        alert("change!!" + $(e.target).val());
      })
      .select(function () {
        $(this).next("span").html("select");
      });
  </script>
</body>
```

- submit, val

```html
<body>
  <p>Type'correct' to validate.</p>
  <form action="javascript:alert('success!');">
    <div>
      <input type="text" />
      <input type="submit" />
    </div>
  </form>
  <span></span>
  <script>
    $("form").submit(function(){
      if(("input:first").val()== "correct"){
        $("span").text("validated...").show();
        return true;
      }
      $("span").text("Not Valid!").show().fadeOut(1000);
      return false // 이후 동작이 실행되지 않음 - default behavior
    })
    <script>
</body>
```

# 탐색(traversing)

-

[참고]

생활코딩-jQuery
