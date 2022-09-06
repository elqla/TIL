- [docker설치](https://docs.docker.com/get-docker/)
- wsl세팅
  - 제어판 hyper-v 켜기
  - cpu 가상화 설정

```bash
docker --version
docker run -d -p 9002:8080 -p 50000:50000 -v /var/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins3 -u root jenkins/jenkins:lts-jdk11
> http://localhost:9002 접속
docker logs jenkins3 - 비밀번호 확인
```

```
이때, 위에 명시된 jenkins3이라는 name을 같게 맞추어주어야한다.
```

![image-20220617210734746](images/image-20220617210734746.png)

![image-20220617211556890](images/image-20220617211556890.png) 

http://localhost:9002/



![image-20220616160348448](images/image-20220616160348448.png) 

![image-20220616160702531](images/image-20220616160702531.png) 

jenkins 컨테이너안 도커 설치

```
컨테이너 진입: docker exec -it jenkins3 bash
도커 설치: curl https://get.docker.com/ > dockerinstall && chmod 777 dockerinstall && ./dockerinstall
```



- 도커라이징 및 배포 설정

  ![image-20220617182550357](images/image-20220617182550357.png) 

```
jenkins에서 newitem클릭
```

![image-20220617182838999](images/image-20220617182838999.png) 



![image-20220617182933075](images/image-20220617182933075.png) 

![image-20220617183000768](images/image-20220617183000768.png) 

![image-20220617183057974](images/image-20220617183057974.png) 

```
docker build -t hello_ssafy:latest .
docker run -d -p 85:80 hello_ssafy # 80:80등 사용하지 않는 포트 적기
```

build now click

 ![image-20220617212914046](images/image-20220617212914046.png) 



![image-20220617212924662](images/image-20220617212924662.png) 

```
npm run build         ##vue 설치
```

![image-20220617214813366](images/image-20220617214813366.png) dist안의 것들을 밖으로 빼줌

```
docker build -t hello_ssafy:latest .
docker run -d -p 86:80 hello_ssafy    # 포트 변경
```



![image-20220617214939331](images/image-20220617214939331.png) 

