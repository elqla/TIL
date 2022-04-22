# pjt 07

#### 이번 pjt를 통해 배운 내용

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작 
- Django web framework를 통한 데이터 조작  
- ORM(Object Relational Mapping)에 대한 이해  
- Django Authentication System에 대한 이해 
- Database many to one relationship(1:N)에 대한 이해



## accounts app

### templates

```django
<!--change_password templates-->
{% extends 'base.html' %}

{% block content %}
  <h1>비밀번호변경</h1>
  <hr>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'movies:index' %}">back</a>
{% endblock content %}
```

- 이외 account app templates 구조 동일

### admin

```python
#pjt07/settings.py
AUTH_USER_MODEL = 'accounts.User'


#models.py
from django.db import models
from django.contrib.auth.models import AbstractUser  #장고에서 제공하는 로그인기능

class User(AbstractUser):
    pass
    
#forms.py
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # 현재 장고프로젝트 모델의 활성화된 User를 참조함
        fields = ('email', 'first_name', 'last_name',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)                   
```

- 처음 모델을 만들때, user 를 셋팅해주었다.



## movies app

```html
<!--detail.html-->
	<h2>댓글목록</h2>
      {% for comment in comments %}
        <li>
          {{ comment.user }}
          -
          {{ comment.content }}
          {% if request.user == comment.user %}
            <form action="{% url 'movies:comment_delete ' comment.pk %}" method="POST">
              {% csrf_token %}
              <input type="submit" value="delete">
            </form>
          {% endif %}
          {{ comment_form }}
        </li>
      {% endfor %}
```

- 댓글창을 구현하는 방법, 그리고 요청이 온 사용자와 코맨트를 작성한 사용자가 같을떄만, 삭제할 수 있는 기능을 부여해주었다. 

```python
#views.py
@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()  # 역참조를 하는 부분
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)
```

- 하나의 영화에 댓글을 달때, 이 댓글이 어떤 게시물에 작성되어야 하는 것인지 모르므로 역참조기능인

  `set.all`을 사용해주었다.

  

### django_ignore

django ignore파일을 초기 생성시 , dbsqlite3가 함께 존재하여 상대에게 내가 작성한 정보를 넘겨주지 못하고 ignore됐다.

이 부분을 잊고 dbsqlite를 지운 파일만 사용하였어서, 페어플레이를 하며 새로 배울 수 있었다.



### 후기

- 이전 프로젝트와 달리 이번 프로젝트에선 1:N관계를 설정해주었다.

- 각 댓글마다, 하나의 게시물을 참조하는 역참조 방식을 적용해볼 수 있었다.

- 또한 accounts앱을 새로 만들어서 로그인, 회원가입, 비밀번호 변경, 로그아웃, 회원정보삭제, 회원정보수정의 기능을 해볼 수 있었다.
