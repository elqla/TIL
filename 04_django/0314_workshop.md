```sqlite
--1
CREATE TABLE countries(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  room_num TEXT NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  grade TEXT NOT NULL,
  price INTEGER NOT NULL
  );
  
--2
INSERT INTO countries VALUES (1, 'b203','2019-12-31', '2020-01-03', 'suite', 900);
INSERT INTO countries VALUES (2, '1102','2020-01-04', '2020-01-08', 'suite', 850);
INSERT INTO countries VALUES (3, '303','2020-01-01','2020-01-03', 'deluxe', 500);
INSERT INTO countries VALUES (4, '807','2020-01-04','2020-01-07', 'superior', 300);

--3
ALTER TABLE countries RENAME TO hotels;

--4
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

--5 분류 .. 내림차순
SELECT grade, count(grade) FROM hotels GROUP BY grade ORDER BY count(grade) DESC;

--6 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오
SELECT *FROM hotels WHERE room_num LIKE 'B%' OR grade = 'deluxe';

--7 지상층 객실이면서 
SELECT * FROM hotels 
WHERE room_num NOT LIKE 'B%' 
AND check_in = '2020-01-04'
ORDER BY price;
```
