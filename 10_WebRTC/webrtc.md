# Websocket을 이용한 채팅 기능 구현



[WebRTC API - Web API | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/web/API/webrtc_api)

- SockJS, Stomp

## SockJS

Websocket polyfill 라이브러리

- [GitHub - sockjs/sockjs-client: WebSocket emulation - Javascript client](https://github.com/sockjs/sockjs-client)

```js
const sock = new SockJS('api/v1/ws');
sock.ononpen = function(){
    console.log('open');
    sock.send('test');
};
sock.onmessage = function(e){
    console.log('message', e.data);
    sock.close();
};
sock.onclose = function(){
    console.log('close');
};
```

## Stomp

https://github.com/stomp-js/stompjs

https://stomp.github.io/stomp-specification-1.2.html

- 특정 토픽에 대한 구독(subscribe)이 가능해짐. 해당 토픽으로 타 클라이언트가 메시지를 send하면, 그 토픽을 구독하는 클라이언트 모두가 메시지를 받게 됨.

https://spring.io/team/rstoyanchev

```js
const socket = new SockJS('api/v1/ws');
const stompClient = Stomp.over(socket);

//SockJS와 stomp client를 통해 연결 시도
stompClient.connect({}, function(frame){
    console.log('Connected: ' + frame);
    stompClient.sunscribe('/topic/greetings', function(msg){
        //hello 출력
        console.log(msg);
});
    //hell0전송
    stompClient.send('/topic/greeting', {}, 'Hello!'))
});
```









# 개발 환경 설정

## api test 도구

- postman
- [Boomerang](https://boomerangapi.com)
- [insomnia](https://insomnia.rest)
- 크롬
  - Network 탭 기능: front-end에서 api요청 및 응답 정보 확인 가능

## Docker

[windows](https://www.docker.com/get-started)