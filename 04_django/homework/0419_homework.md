1. ```
   MTV pattern
   model, templates, view
   model은 데이터구조 정의, 기록 관리(추가, 수정, 삭제)
   templates은  파일의 구조, 레이아웃 정의, 보여줄 화면
   view는 http 요청 수신, 응답, 데이터에 접근
   ```

2. ```python
   from articles import views
   path('', views.index)
   ```

3.  templates and static Django 프로젝트는 기본적으로 render 할 html과 같은 template 파일과 css, js와 같은 static 파일을 앱 폴더 내부의 templates와 static 이름의 폴더에서 찾는다.  만약 해당 위치가 아닌 임의의 위치에 파일을 위치 시키고 싶으면 __(a)__ 파일의 __(b)__와 __(c)__ 라는 변수에 담긴 리스트의 요소를 정의하면 된다.  빈칸 (a), (b), (c)에 들어갈 내용을 작성하시오.
   
   ```python
   #project/settings.py
   a) settings.py
   b) templates = []
   c) STATICFILES_DIRS = [
       BASE_DIR / 'static', # 추가적인 경로 필요할때 만들기
   ]
   ```
   
4. ```python
   python manage.py makemigrations
   python manage.py showmigrations
   python manage.py sqlmigrate
   python manage.py migrate
   ```

5. ```python
   1) F
   2) T
   3) F
   4) T 
   meta클래스는 모델 폼을 사용할 경우, 사용할 모델의 정보를 작성하는 곳이다. fields로 어떤걸 가져올지 정의
   ```
   
6. ```python
   MEDIA_ROOT = BASE_DIR/ 'media'
   MEDIA_URL = '/uploaded_files/'
   ```

7. ```python
   1) T
   2) F
   3) T
   4) F
   5) F
   ```

8. on_delete 게시글과 댓글의 관계에서 댓글이 존재하는 게시글은 삭제할 수 없도록 즉, ProtectedError를 발생시켜 참조 된 객체의 삭제를 방지하는 __(a)__를 작성하시오
   
   ```python
   Protect
   ```
   
9. ```python
   a) ManyToManyField
   b) related_name
   ```

10. ```python
    tablename = accounts_user_followings
    coloumn = from_user_id, to_user_id









