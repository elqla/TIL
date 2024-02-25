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

### LeftJoin, InnerJoin

- LeftJoin (Right Join)

  - 한쪽이 없을떄 그냥 null로 합침

  - 왼쪽 테이블의 모든 행을 포함하며, 오른쪽 테이블에서 일치하는 행이 있는 경우에만 해당 행을 반환합니다.
    만약 오른쪽 테이블에서 일치하는 행이 없는 경우에도 왼쪽 테이블의 모든 열은 결과에 포함되지만, 오른쪽 테이블의 열은 NULL로 채워집니다.

- InnerJoin

  - 양쪽 데이터가 둘다 있을때 합침

  - 두 테이블 간의 일치하는 행만 반환합니다. 즉, 양쪽 테이블에서 조건에 부합하는 행들만을 결과로 가져옵니다.
    만약 어떤 행이 한 쪽 테이블에는 있지만 다른 쪽 테이블에는 없는 경우, 해당 행은 결과에서 제외됩니다.

- OuterJoin

  - 데이터가 양쪽 다 존재여부 상관없이 합침

### int로 변경해서 받기

```js
// controller에서

@Get(":name")
getSpecificChannel(@Param("id", ParseIntPipe)id: number){}

// 또는 main.ts 에서
// transform: true해주면 됨.
// npm i class-transformer
app.useGlobalPipes(
    new ValidationPipe({
      transform: true,
    }),
  );


```
