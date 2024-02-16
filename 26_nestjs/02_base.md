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

- res 를 받아서 쓰면 return req.json(user) 이런식으로 쓰는건 지양.

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
