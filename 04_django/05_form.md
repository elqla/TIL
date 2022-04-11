# FORM

## django Form class

- django's form
  - form과 관련된 유효성 검사 단순, 자동화
  - 안전하고 빠름
    - 랜더링을 위한 데이터 준비 및 재구성
    - 데이터에 대한 html 폼 생성
    - 클라이언트로부터 받은 데이터 수신 및 처리

[FORM](https://docs.djangoproject.com/en/3.2/topics/forms/)

[WIDGET](https://docs.djangoproject.com/en/3.2/ref/forms/widgets/)

[Coding style](https://docs.djangoproject.com/en/3.2/internals/contributing/writing-code/coding-style/)

- Form 선언

  - 파일위치: `app폴더/forms.py`권장
  - model에 써도 되나, 관리 불편

  ```python
  # articles/forms.py
  from django import forms
  class ArticleForm(forms.Form): #forms모듈의 form 클래스를 부모클래스로 상속을 받는다.
      REGION_A = 'sl'
      REGION_B = 'dj'
      REGION_C = 'gj'
      REGIONS_CHOICES ={
          (REGION_A, '서울'),  # 튜플의 우측, 사용자에게 보이는 값
          (REGION_B, '대전'),
          (REGION_C, '광주'),
      }
  
      title = forms.CharField(max_length=10)
      content = forms.CharField(widget=forms.Textarea) #forms.model 
      ## 위젯 ! field를 먼저 지정을 하고, 추가로 작성 !
      region = forms.ChoiceField(widget=forms.Select, choices=REGIONS_CHOICES)
  ```

  ```python
  # model form으로 변경
  # model과 중복해서 사용하지 않으려고 !
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm): # baseModelform을 상속받아 사용함
      class Meta:  # forms library의 모델 폼을 상속받고, meta 클래스를 선언
          model = Article    # 만들었던 모델이 무엇인지 설정
          fields = '__all__'  # 전체 필드 출력 (문자열)
          #exclude = ('title',) #fields와 exclude 동시에 쓸 수 없음/출력제외시 exclude
  ```

  

- Form 사용하기

  ```python
  #view.py
  from .forms import ArticleForm
  
  def new(request):
      form = ArticleForm() # class로 instance 만들기
      context = {
          'form':form
      }
      return render(request, 'articles/new.html', context)
  ```

- new.html

  ```django
  {% extends 'base.html' %}
  
  
  {% block content %}
    <h1>NEW</h1>
    <hr>
    
    <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      {% comment %} <label for="title">Title: </label>
      <input type="text" id="title" name="title"><br>
      <label for="content">Content: </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea> {% endcomment %}
      <input type="submit">
    </form>
    <a href="{% url 'articles:index' %}">back</a>
  {% endblock content %}
  ```

  

- Form rendering options

  - label, input 쌍에 대한 출력 옵션

    - as_p()
      - 각 필드가 단락 <p> 로 감싸져 렌더링됨
    - as_ul()
      - 각 필드가 목록항목 <li>로 감싸져서 렌더링됨
      - <\ul> 은 직접 작성
    - as_table()
      - 각 필드가 <tr> 행으로 감싸져서 렌더링 됨
      - </table> 태그는 직접 작성할 것

    

- django의 HTML input 요소 표현 방법 2가지
  - Form fields
    - `input 에 대한 유효성 검사 로직을 처리`하며 템플릿에서 직접 사용됨
  - Widgets
    - django html input element 표현
    - HTML 렌더링
    - GET/POST 딕셔너리에서 데이터 추출
    - widgets은 반드시 form fields에 할당됨

## model form

- django Form을 사용하다보면, 모델 필드 재정의 행위 중복 됨

- Meta class
  - model의 정보를 작성하는 곳
  - modelform을 사용할 경우 사용할 모델이 있어야 하는데, metaclass가 이를 구성함
  - `inner class`
    - 클래스 내에 선언된 다른 클래스
    - 관련 클래스 그룹화, 가독성 및 유지관리
    - 외부 에서 내부 클래스에 접근 x, 코드의 복잡성 줄임
  - `metadata`
    - 데이터에 대한 데이터
    - 사진촬영-사진데이터-사진의 메타데이터(촬영 렌즈 조리개값)

- `is_valid()` 메소드
  - 유효성 검사 실행

- `save()` 메소드
  - form에 바인딩된 데이터에서 데이터베이스 객체를 만들고 저장
  - 모델폼의 하위 클래스는 `기존 모델 인스턴스`를 `키워드 인자 인스턴스`로 받아들일 수 있음

- form Vs modelform

  - form

    - 어떤 모델에 저장해야하는지 알 수 없으므로, 유효성 검사 이후 cleaned_data dictionary 생성
    - 모델과 연관 없는 데이터 받을때 사용

  - modelform

    - 장고가 해당 모델에서 양식에 필요한 대부분의 정보를 이미 정의

    - 어떤 레코드를 만들어야할 지 알고있으므로 `바로 save() 가능`

      

- view

- ```
  create + new -> create (new.html->create.html)
  update + edit -> update(edit.html->update.html)
  url #
  ```

  ```python
  # view.py // 
  def new(request):
      form = ArticleForm() # class로 instance 만들기
      context = {
          'form':form
      }
      return render(request, 'articles/new.html', context)
  
  
  def create(request):
      form = ArticleForm(request.POST)
      # 유효성 검사
      if form.is_valid():  # modelform의 메서드
          article = form.save()   # save가 return 값이 있음
          return redirect('articles:detail', article.pk)
      #print(form.errors) # error메서드 담아서 줌 
      return redirect('articles:new')  # else # 제목이 10자 초과
      
      # title = request.POST.get('title')
      # content = request.POST.get('content')
      # article = Article(title=title, content=content)
      # article.save()
      #return redirect('articles:detail', article.pk)
  ```

  ```python
  def create(request):
      if request.method == "POST":   # post먼저 !! post일때만 db 조작 ! 
          #create
          form = ArticleForm(request.POST) # request요청을 받은거고, POST에 정보가 담겨서 그걸 줌 !
          if form.is_valid(): 
              article = form.save()   
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm() # class로 instance 만들기  # 빈 폼이 저장됨 !
      context = { 
          'form':form
      }    # is_valid 통과하지 못했을때 포함else로 안가고 return시, context가 없어서.
      return render(request, 'articles/create.html', context)  
  # view, new.html변경
  ```



- 위젯 활용하기

  ```python
  class ArticleForm(forms.ModelForm): #forms모듈의 form 클래스를 부모클래스로 상속을 받는다.
      # 위젯을 쓰려면, 모델폼이여도 form에서 정의해줘야함
      title = forms.CharField(
          widget=forms.TextInput(
              attrs={  # 위젯의 속성값을 attribute라는 키워드 인자의 딕셔너리에 넣어줘야함
                  'class':'my-title',  # 부트스트랩 여기서 함
                  'placefolder':'Enter the title',
              }
          )
      )
      content = forms.CharField(
          widget=forms.Textarea(
              attrs={
                  'class':'my-content',
              }
          )
          error_messages=(
              'required':'Please enter your content!!!'  # error메세지 변경
          )
      )
      class Meta:  # forms library의 모델 폼을 상속받고, meta 클래스를 선언
          model = Article    # 만들었던 모델이 무엇인지 설정
          fields = '__all__'  # 전체 필드 출력 (문자열)
          #exclude = ('title',) #fields와 exclude 동시에 쓸 수 없음/출력제외시 exclude
          
  ```



## Rendering fields manually

- 수동으로 form 작성하기
  - rendering fields manually

[django rendring fields manually](https://docs.djangoproject.com/en/3.2/topics/forms/#rendering-fields-manually)

- `create.html`

```django
{% extends 'base.html' %}

{% block content %}
  <!-- {{ request.resolver_match }} -->

  <h1>CREATE</h1>
  <hr>

  <form action="{% url 'articles:create' %}" method="POST">
    <!--html form action이 없으면, 현재 url로 action을 보냄 다만 권장 x-->
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>

  <h2>1. rendering fields manually</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <div>
      {{ form.title.errors }}
      <!--라벨 출력-->
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>
    <div>
      {{ form.content.errors }}
      {{ form.content.label_tag }}
      {{ form.content }}
    </div>
    <input type="submit">
  </form>

  <h2>2. looping over the form's fields</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% for field in form %}
      {{ field.errors }}
      {{ field.label_tag }}
      {{ field }}
    {% endfor %}
    <input type="submit">
  </form>

  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```



## bootstrap form

- 부트스트랩에서 form 검색 

  ```python
      title = forms.CharField(
          widget=forms.TextInput(
              attrs={  # 위젯의 속성값을 attribute라는 키워드 인자의 딕셔너리에 넣어줘야함
                  'class':'my-title form-control',  # 부트스트랩은 각 클래스에 추가하기
                  'placefolder':'Enter the title',
              }
          )
      )
  ```

- 라이브러리 사용

  [django-bootstrap-v5](https://django-bootstrap-v5.readthedocs.io/en/latest/)

  ```python
  $ pip install django-bootstrap-v5
  $ pip freeze > requirements.txt
  INSTALLED_APPS = [
      'bootstrap5',
  ```

  ```django
  #html
  {% load bootstrap5 %}
    <form action="{% url 'articles:update' article.pk %}" method="POST">
      {% csrf_token %}
      {% bootstrap_form form %}  <!--커스텀이 더 어려워진다..-->
      <!--{{ form.as_p }}-->
  ```

  ```django
      {% for field in form %}
        {% if field.errors %}
          <!--errors는 에러들의 목록-->
          {% for error in field.errors %}
            <div class="alert-danger">{{ error }}</div>
          {% endfor %}
        {% endif %}
        <!--{{ field.errors }}-->
        {{ field.label_tag }}
        {{ field }}
      {% endfor %}
  ```
  
  

```
noreversematch
url만 보면 된다. templates url
```

```
redirect ; url로 보냄
- 데이터 베이스와 동일하게 저장되나 ?  모델 폼 사용하는게 간편

  

- 단순히 데이터로만 사용되는가 ? 

- 폼  ( 데이터로써만 사용하기 때문에 모델과 연관성이 없다. meta에 넣어서 참조할 모델이 없음)

- 폼의 의도는 input, model field
```
