### StatefulWidget Lifecycle

1. initState
   위젯이 호출될 때 한 번 호출됨, 위젯이 화면에 그려지기 전이므로 build method보다 먼저 호출된다.
   State class에서 값을 초기화할때 사용한다.
   -> BuildContext속성에는 접근할 수 없다.
2. build
   State의 build메소드는 StatelessWidget의 build메소드와 동일하다.
   재정의가 항상 필요한 메소드이다.
   사용자 인터페이스를 생성하고 initState메소드 이후에 해당 상태를 호출할 때마다 트리거된다.
3. dispose
   dispose메소드는 위젯이 위젯 트리에서 제거되기 직전에 호출된다.
   따라서 dispose메소드를 사용하여 해제해야 하는 리소스를 정리할 수 있다.

---

참고
https://nayotutorial.tistory.com/46
