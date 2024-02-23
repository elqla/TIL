### @nestjs/passport

Authentication

https://docs.nestjs.com/security/authentication

```cmd

npm i @nestjs/passport passport passport-local

```

@Injectable 붙으면 다 프로바이더임.
다른 폴더 모듈이면 import

service안에 service를 두고 있어도 되는가?
= 되지만 테스트할때 모킹하는게 귀찮아지므로,, repository사용 권장

컨트롤러 안에서만 서비스
서비스에선 레포지
레포지는 엔티티만 하고..

### typeorm transaction

- save = insert into

- 다만 여러 save중 하나만 된다거나 했을떈? -> transaction을 쓰면 됨.

- transaction 사용 방법도 여러개임

- queryRunner 쓰기
