### 1. Axis (축), Grid helper

-

```js
const axesHelper = new THREE.AxesHelper(5); // 축 생김
// camera.position 조정
// mesh.position 조정
scene.add(axesHelper);
```

```js
const gridHelper = new THREE.GridHelper(2);
scene.add(gridHelper);
```

### 2. FPS (초당 프레임 수) 체크하기

- npm i stats.js
- 개발자 도구 끄고 테스트 (성능 버벅일 수 있음)

```js
const stats = new Stats();
document.body.append(stats.domElement);
function draw() {
  stats.update();
}
```

### 3. GUI 컨트롤

- npm i dat.gui

```js
const gui = new dat.GUI();
gui.add(
  mesh.position, // 무엇
  "y",
  -5,
  5,
  0.01 //step
);

// 또는
gui
  .add(
    mesh.position, // 무엇
    "y"
  )
  .min(-10)
  .max(3)
  .step(0.01)
  .name("메쉬의 Z위치");

gui.add(camera.position, "x", -10, 10, 0.01).name("카메라x");
camera.lookAt(mesh.position); // 카메라가 언제나 mesh를 바라보도록
function draw() {
  camera.lookAt(mesh.position); // 여기도 추가해줘야 함.
}
```
