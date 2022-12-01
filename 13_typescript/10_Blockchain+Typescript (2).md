```bash
npm init -y
# -D devDependencies
npm install -D typescript
# 타입스크립트로 작업한다는 것을 알림
touch tsconfig.json
# 빌드 없이 빠르게 새로고침 하고 싶을떄
npm i -D ts-node
# 서버를 재시작하지 않고, 자동으로 커맨드를 재 실행해줌
npm i nodemon
# 
npm i -D @types/node
```

- package.json

```json
{
  "name": "typechain",
  "version": "1.0.0",
  "description": "",
  "main": "",
  "scripts": {
    "build": "tsc",
    "dev": "nodemon --exec ts-node src/index.ts",
    "start": "node build/index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "ts-node": "^10.9.1",
    "typescript": "^4.8.2"
  }
}

```

- tsconfig.json

```json
{
  // 작업하고싶은 모든 디렉토리를 넣어줌
  "include": ["src"],
  // outdirectory: 자바스크립트 파일이 생성될 위치 지정
  // pakage.json에   
  // "scripts": {
  //   "build": "tsc"
  // }, 추가 후 실행
  "compilerOptions": {
    "outDir": "build",
    "target": "ES6", // 컴파일시, javascript version 설정 가능
    "lib": ["ES6", "DOM"], // runtime환경, 어떤 API를 사용하고, 어떤 환경에서 코드를 실행하는지 알려줌
    //dom: document.했을때 ts가 알 수 있음. 
    "strict": true
  }
}
```

- npm으로 자바스크립트 패키지를 받아올 때 해결방법

```js
//myPackage.js
export function init(config){
  return true;
}
export function exit(code){
  return code + 1
}
```

```typescript
//index.ts
import {init, exit} from 'myPackage'   //여기 myPackage를 import !
init({
  url:"true"
})
exit(1)
localStorage.clear()
```

```tsx
//myPackage.d.ts
// typescript에게 타입을 알려주기 위함

interface Config{
  url:string
}

declare module "myPackage"{
  function init(config: Config): boolean
  function exit(code: number): number
}
```



- ts 와 js 파일이 같이 있는 경우
  - 주로 Typescript -> Javascript로 마이그레이션 할때

```json
//tsconfig.json
{
  ...
    "esModuleInterop": true,
    "allowJs": true
}
```

```typescript
//index.ts
import { init, exit } from "./myPackage";
```

