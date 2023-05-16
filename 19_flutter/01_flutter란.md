### 플러터를 사용한 서비스

- [wonderous](https://flutter.gskinner.com/wonderous/)

- [flutter_showcase](https://flutter.dev/showcase)

- i/o photobooth

- Flokk

### How Flutter Works?

- [architecture](https://docs.flutter.dev/resources/architectural-overview)

![Alt text](https://docs.flutter.dev/assets/images/docs/arch-overview/archdiagram.png)

- os(ios, android, window)에 버튼 만들어달라고 하는게 기존 시스템이라면 플러터는 os에 의존하지 않음.

- 앱 실행 -> 플랫폼 (runner project) -> 엔진 가동 (c, c++) -> 다트(플러터)코드 동작 -> UI그려짐

- 단점: native widget을 사용하지 않는다는 것이 문제점.

  - ios처럼 비슷하게 만들려고 하나 native(operating system)에 의해 실행되지 않기 때문

- 장점: OS에 국한되지않는다는 것.

### Flutter VS ReactNative

React Native -> Js -> OS

Flutter -> Engine -> ComponentRender
