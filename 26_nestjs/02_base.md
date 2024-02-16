## 1. Express와 비교

express + sequalize

middleware

## 2. NEST 기초

### 1) Controller

1. @Controller('user') == router

   // Decorator

   @Get('sub_path')

2. Controller를 만들면, Module의 컨트롤러 공간에 추가해야함.

다만, 네스트가 안쓰면 알려줌.

### 2) Service

1. service역할은 비즈니스 로직

2. express에서 각각 코드짜서 모킹해줘야하는걸 분리됐기 때문에 편하게 해줄 수 있음.

- express middleware에서도 분리해줄 수 있다.

  하지만 직접만들고 하다보면 코딩스타일이 달라짐 -> nest쓰는게 나음.

- 응답이 같은 경우 return {code: 'SUCCESS', data: user} 이런식으로 api return 을 줄때
  이걸 interceper 하나로 만들 수 있음.

- res 를 받아서 쓰면 return res.json(user) / 실제데이터말고 가짜데이터로 하고싶을떄도 불편함.

3. 분리 이유.

- service: 요청, 응답에 대해선 알지 못함.

  - req, res 안쓰는게 좋음

- controller: 요청, 응답에 대해서 한번에 처리

  - req, res 알아야함.

```js
// Service
import { Injectable } from "@nestjs/common";

@Injectable()
export class AppService {
  getUser(): string {
    const user = await User.findOne();
    return user;
  }
}
```

```js
//Controller
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('user')
  getUser(): string {
    return this.appService.getUser();
  }
}
```

### 3) Implement, Injectable(DI) 알아보기

Implement: TypeScript검사. Error Fix

Injectable: Dependency Injection, Provider

- Injectable을 쓰면 providers에 넣어줘야함..

nest 는 의존성 주입을 해주고, 그걸 프로바이더를 통해함.

예를들면, controller에서

```js
@Controller()
export class AppController{
  constructor(private readonly appService: AppService){
    // 기존이라면
    // this.appService = AppService해줘야하는데. 안해줘도 됨.
  }
  @Get()
  getHello(){
    console.log('hello')
    return this.appservice.getHello();
    // new AppService().getHello()--- noooo
  }
}

new AppController(new AppService());

// test할때는 ..  예를들면 이런식으로 쓸 수 있다. !
new AppController(new TestAppService())

```

DB에 salt 값 저장

JAVASCRIPT는 대부분 HEAP에 저장, 호출 스택은 스택에 저장..

Service로 분리했기 때문에 무거워지면 또 분리를 하면 됨

다른 서비스에서 constructure(private..)로 또 가져올 수 있음

log
sentry, databook, aws cloudwatch - 활용하지 않는 데이터 저장 안하거나 nosql

salt..에...

controller -> service -> repository -> entity

- pm2 로 하고, 로드밸런서 따로 붙임

- 싱글코어로 함.. 여러개 돌ㄹ..ㅣ..ㅁ.. aws, code deploy
