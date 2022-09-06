

## 백엔드 구동을 위한 사전 필요사항

도커 허브에서 데이터베이스 도커 이미지를 가져와, 프로젝트에 필요한 db스키마가 적용된 mysql 컨테이너를 바로 실행

```bash
# 도커 이미지 다운로드
docker pull noncelab/nft-mysql
# 도커 이미지 확인
docker images
# 컨테이너 실행
docker run -d -p 3306:3306 --name nft-mysql noncelab/nft-mysql
# 컨테이너 실행 확인
docker ps -a
```

컨테이너 실행 확인 후 접속 정보를 통한 db활용가능

```bash
# 도커 컨테이너 실행 로그 보기
docker logs -f nft-mysql
# 도커 컨테이너 중지 및 실행
docker stop nft-mysql [혹은 컨테이너 아이디]
docker start nft-mysql
```

mysql 클라이언트 프로그램을 사용하여 도커 컨테이너에 접속
기본 포트번호 3306
접속시 유효한 정보를 백엔드설정.env에도 적용하여, db에 올바르게 접속하여 사용할 수 있도록 합니다.

`url, id, password`