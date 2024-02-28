### 자동화

- src folder/spec => unit test (단위 테스트)

  - service 파일에 실제 Repository를 mocking할 데이터로 바꿔주기

  - 아니면 디비 건들이게 됨.

  - beforeEach는 각각의 it 전에 실행됨.

    service를 새로 할당함.

- 돈, 에러난거 위주 테스트

  npm test

## ------------------------

### E2E Test

- test folder => e2e test (end to end)

  - 실제 컨트롤러에 요청 및 응답 확인

- src와 무관함.

- test용 디비를 하나 더 만들어서 그쪽에 요청 보내도록 연결하기

- process.env.NODE_ENV === 'test' (e2e test 시)

환경은 똑같이 하나, 디비를 바꿈

npm run test:e2e
