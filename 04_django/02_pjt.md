[The staticfiles app](# The staticfiles app)



### 1. name space

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, INSTALLED_APPS에 작성한 app 순서로 tamplate을 검색 후 렌더링

- 임의로 templates의 폴더 구조를 `app_name/templates/app_name` 형태로 변경해 임의로 이름 공간 생성 후 변경된 추가 경로 작성

- url namespace (app_name, 참조)
  - views == `'index.html'`-> `'appname/index.html'`  파일을 렌더링해줘
    - redirect시엔, `appname:variable`
  - html == `{% url 'appname:variable' %}`  ㅇㅇ로 요청을 보내줘

```python
#articles/urls.py
app_name = 'articles' #써주기 
urlpatterns = [...]

#articles/index.html
  <a href="{% url 'dinner' %}">dinner</a>
    
=><a href="{% url 'articles:dinner' %}">dinner</a>
  <a href="{% url 'pages:index' %}"></a>
```

- template namespace
  모아서보는 장고의 특성 => 추가경로를 작성 (중간경로)

```python
#articles/templates/articles 생성 (앱과 같은 이름의 폴더)
기존의 templates의 html 이동시킴
새로 생긴 articles가 templates의 namespace 역할을 함

#articles/views.py
def index(request):
    return render(request, 'index.html')
=>def index(request):
    return render(request, 'articles/index.html')

#templates/base.html
{% include 'articles/_nav.html' %}
```



### 헷갈리는 개념 잡기

```python
# url: namespace 분리(app_name의 name url을 실행시켜줘)
return redirect('articles:detail', article.pk)
# redirect:url로 요청을 보내줘

-------------------------------------------------------
# rendering
return render(request, 'articles/detail.html', context)
# articels 템플릿 안에 있는걸 찾을건데(물리적인 위치) detail.html 파일을 렌더링
```



### 2. static files

- url에 있는 자원(resource)를 요청(http request)받아 제공(serving)하는 응답(http response)을 처리:: 기본동작
- 사진파일: 자원
- 파일경로: 웹 주소
- 즉, server는 요청받은 url로 정적자원을 제공

```django
{% load static %}
<img src = "{% static 'my_app/example.jpg' %}" alt="My image">
ex) my_app/static/my_app/example.jpg

#temp 에선 app/templates/
#ststic은 app/static/app/
```



(1) STATICFILES_DIRS = [BASE_DIR/ 'static',]

(2) STATIC_URL = '/static/'

​	STATIC_ROOT에 있는 저적 파일 참조시 사용할 url

​	실제파일, 디렉토리가 아님 url로만 존재

​	비어있지 않은 값으로 설정시, 반드시 / 로 끝나야 함

(3) STATIC_ROOT

​	collectstatic이 배포를 위해 정적파일을 수집하는 디렉토리의 절대 경로, 장고의 모든 정적 파일을 모아넣음

 - 개발 settings.py의 DEBUG = True       #개발단계에서는 동작하지 않는다 !

 - 배포 settings.py의 DEBUG = False 

   - AllOWED_HOST = [*]

   - 참고

     ```python
     #settings.py
      STATIC_URL = '/static/'
      STATIC_ROOT = BASE_DIR / 'staticfiles'
     -------------------------------------------
     $python manage.py collectstatic
     ```

- app안에 static 폴더 만들기

  




#### django template tag

- load

  - 템플릿 태그세트 로드
  - 라이브러리, 태그, 필터

- static

  ```django
  {% load static %}   #built in XX
  <img src = "{% static 'my_app/example.jpg' %}" alt="My image">
  ```



`활용`

- 기본경로

```django
#articles/static(생성) img 추가
#articles/templates/articles
{% extends 'base.html' %}
{% load static %}(추가)
{% block content %}
  <img src="{% static 'sample-img.png' %}" alt="" style="width:300px">   #app/static 이므로 바로 이미지 삽입

이미지 url경로 보면 STATIC_URL = '/static/'쓰인걸 볼 수 있음  (즉, url로만 쓰임)
```

- ![image-20220304110859934](images/image-20220304110859934.png).

  ```django
    <img src="{% static 'articles/sample-img.png' %}" alt="" style="width:300px">
  ```

```python
STATIC_URL = '/static/'
밑에 추가하기
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

![image-20220304111351381](images/image-20220304111351381.png).

```django
#templates/base.html
  {% block style %}{% endblock style %}

#articles/templates/articles/index.html
{% block style %}
<link rel="stylesheet" href="style.css">  #이렇게 쓰면 장고에선,  static 파일 못불러옴
{% endblock style %}

=> <link rel="stylesheet" href="{% static 'style.css' %}">

```

### media root

```

MEDIA_ROOT = BASE_DIR/ 'media'
MEDIA_URL = '/media/'

    'imagekit',
    
    
    
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField
    upload_picture = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(500, 500)],
        format='JPEG',
        options={'quality': 60})
    #image = models.ImageField(upload_to="images/", blank=True)
    
    
    
    
#pjt_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('articles.urls')),
    # path('accounts/', include('accounts.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # static

```





---

---

## The staticfiles app

> https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/#module-django.contrib.staticfiles

**`STATICFILES_DIRS`**

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

- app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

<br>

**`STATIC_URL`**

```python
STATIC_URL = '/static/'
```

- STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL 
- 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로 (기본 경로) 및STATICFILES_DIRS에 정의된 추가 경로들을 탐색함 
- 실제 파일이나 디렉토리가 아니며, URL로만 존재 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

<br>

**`STATIC_ROOT`**

- collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로 
- django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로 
- 개발 과정에서 setting.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음 
  - (배포시, False)
  - AllOWED_HOST = [*]
- 직접 작성하지 않으면 django 프로젝트에서는 setting.py에 작성되어 있지 않음 
- 실 서비스 환경(배포 환경)에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함

> [참고] **collectstatic**
>
> - 프로젝트 배포 시 흩어져있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업
>
> ```python
> # settings.py 예시
> 
> STATIC_ROOT = BASE_DIR / 'staticfiles'
> ```
>
> ```bash
> $ python manage.py collectstatic
> ```

<b

<br>

### static file 사용하기

1. 기본경로

   - `article/static/articles/` 경로에 이미지 파일 위치

     ```django
     <!-- articles/index.html -->
     
     {% extends 'base.html' %}
     {% load static %}
     
     {% block content %}
       <img src="{% static 'articles/sample.png' %}" alt="sample">
       ...
     {% endblock %}
     ```

     - 이미지 파일 위치 - `articles/static/articles/`

    - static file 기본 경로

      - `app_name/static/`

2. 추가 경로

   - `static/` 경로에 CSS 파일 위치

```django
<!-- base.html -->

<head>
  {% block css %}{% endblock %}
</head>
```

```python
# settings.py

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

```django
<!-- articles/index.html -->

{% extends 'base.html' %}
{% load static %}

{% block css %}
  <link rel="stylesheet" href="{% static 'style.css' %}">
{% endblock %}
```

```css
/* static/style.css */

h1 {
    color: crimson;
}
```

<br>







