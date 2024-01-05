1. SQL, NOSQL

- MySQL

```

brew install mysql
brew services start mysql
mysql_secure_installation

```

$ mysql -h localhost -u root -p
exit

```
brew install mysqlworkbench --cask
```

$ mysql.server start
$ mysql.server stop

1. db 생성

```
CREATE SCHEMA 'nodejs' DEFAULT CARACTER SET utf8;

use nodejs

show databases
```

```
// database명.테이블명
CREATE TABLE nodejs.comments(
  id INT NOT NULL AUTO_INCREMENT,
  commenter INT NOT NULL,
  created_at DATETIME NOT NULL DEFAULT now(),

)

```
