1.  models.py를 작성한 후 마이그레이션 작업을 위해 터미널에 작성해야 하는 두 개의 핵심 명령어

```bash
$python manage.py makemigrations
$python manage.py migrate
```

2. 새로운 Article을 저장하기 위한 코드

```python
#1
article = Article()
article.title = ""
article.content = ""
article.save()


#2
article = Article(title="", content="")
article.save()

#3
Article.objects.create(title="", content="")
```

3.  Location을 가져오려고 한다.

```python
obj_list=Location.objects.all()
first_element = Location.objects.all()[0] #첫번째요소
last_element = Location.objects.all().reverse()[0] #마지막요소
#articles = Article.objects.all()[::-1] (마지막꺼 먼저 정렬)
또는
locations = list(Location.objects.all())
first_element = locations[0]
last_element = locations[-1]

또는
obj_list.latest('pk')
obj_list.earliest('pk')
obj_list.first() 
obj_list.last()

return render_to_response(template_name, {
        'first_element':first_element,
        'last_element':last_element,
    })

#templates
{{ first_element.terminal_id}} {{last_element.terminal_id}}
```

4. my_post 변수에 Post 객체 하나가 저장되어 있다.  title을 “안녕하세요” content를 “반갑습니다” 로 수정하기 위한 코드를 작성하시오

```python
$ python manage.py shell_plus 
my_post = Post.objects.get(pk=1)
my_post.title = "안녕하세요"
my_post.content = "반갑습니다"
my_post.save()
```

5. 만들어진 모든 Post 객체를 QuerySet형태로 반환 해주기 위해 빈칸에 들어갈 코드를 작성하시오

```python
post = Post.objects.filter()
```

```

```

