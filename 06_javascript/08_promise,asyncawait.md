[TOC]



## 1. Promise

`const fetchResponePromise = fetch(resource [, init])`

![image-20220916234952156](images/image-20220916234952156.png) 

.then이 promise

:star: 중요

![image-20220916235215289](images/image-20220916235215289.png)  

---



## 2. Async Await

- 문제점 (callback 지옥)

![image-20220916235904934](images/image-20220916235904934.png) 

- promise적용으로 해결

![image-20220916235939735](images/image-20220916235939735.png) 



- 인간은 문법적 단순함을 꿈꿈 (오른쪽으로 변경함)
- :star2: 

![image-20220917000155249](images/image-20220917000155249.png) 

- await는 언제나 함수 안에서 실행되야하고, 그 앞에는 async가 붙어있어야 함

`예시`

![image-20220917001413578](images/image-20220917001413578.png) 

async함수는 자동으로 promise를 return 하기에 await를 쓴다.

![image-20220917001325376](images/image-20220917001325376.png) 

만약 return 을 만든다면, return 받은 값을 쓸 수 있음



---

## 3. 내 Promise만들기

![image-20220917001833372](images/image-20220917001833372.png) 

:star: 대부분 함수 안에서 promise를 return해줌

- 좀 더 효율적으로 쓰기 `성공 시 resolve`

![image-20220917001906028](images/image-20220917001906028.png) 



---

`참고`

05_ajax.md

https://www.youtube.com/watch?v=1z5bU-CTVsQ&list=PLuHgQVnccGMBVQ4ZcIRmcOeu8uktUAbxI&index=3

https://www.youtube.com/watch?v=PasFh_t1mhY&list=PLuHgQVnccGMBVQ4ZcIRmcOeu8uktUAbxI&index=4

https://crmrelease.tistory.com/98