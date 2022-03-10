1. Model 반영하기

   ```
   Migrations
   ```

2. Model 변경사항 저장하기

   ```python
   $ python manage.py makemigrations
   $ python manage.py migrate
   
   $python manage.py showmigrations
   ```

3. python shell

   ```python
   $ python manage.py shell_plus
   ```

4. django model field

   ```python
   CharField(max_length=None, **options)
   TextField(**options)
   DateTimeField(auto_now=False, auto_now_add=False, **options)
   EmailField(max_length=254, **options)
   FileField(upload_to=None, max_length=100, **options)
   ```

   