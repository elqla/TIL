[controls](https://threejs.org/docs/index.html?q=controls#api/en/geometries/SphereGeometry)

### 1. OrbitControls

-

```js
// Controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; // 부드럽게 해줌
// controls.enableZoom = false;
// controls.maxDistance = 10;
// controls.minDistance = 3;

// controls.minPolarAngle = Math.PI / 4; // 45도 // 수직방향 회전범위 한정
// controls.minPolarAngle = THREE.MathUtils.degToRad(45);
// controls.maxPolarAngle = THREE.MathUtils.degToRad(135);
// controls.target.set(2, 2, 2); // 회전 중심점 타겟 정해줌
controls.autoRotate = true;
controls.autoRotateSpeed = 5;
```

### 2. TrackballControls

- orbitcontrols과 다른점 : 수직방향 컨트롤 가능함.

```js
// Controls
const controls = new TrackballControls(camera, renderer.domElement);
controls.maxDistance = 20;
controls.minDistance = 5;
// controls.target.set(3, 3, 3);
```

### 3. FlyControls

- 마우스나, 키보드로 움직일 수 있음.

```js
// Controls
const controls = new FlyControls(camera, renderer.domElement);
controls.rollSpeed = 0.1;
// controls.movementSpeed = 3;
// controls.dragToLook = true;

function draw() {
  const delta = clock.getDelta();

  controls.update(delta); // delta넣어줘야함.
}
```

### 4. FirstPersonControls

- flycontrol 의 상위 버전

```js
// Controls
const controls = new FirstPersonControls(camera, renderer.domElement);
// controls.movementSpeed = 10;
// controls.activeLook = false;
controls.lookSpeed = 0.1; // 위의 rollspeed와 비슷
controls.autoForward = true;

function draw() {
  const delta = clock.getDelta();

  controls.update(delta);
}
```

### 5. PointerLockControls

- update메소드 없음.
- esc 사용
- pointer lock api 사용
- canvas.requestpointerlock()

```js
// Controls
const controls = new PointerLockControls(camera, renderer.domElement);

controls.domElement.addEventListener("click", () => {
  controls.lock(); // 동작하기 위해 넣어줘야함. user jesture need
});
controls.addEventListener("lock", () => {
  console.log("lock!");
});
controls.addEventListener("unlock", () => {
  console.log("unlock!");
});
```

### 6. DragControls

- update메소드 없음.
- 매쉬 드래그 조작 가능

```js
const meshes = [];
let mesh;
let material;
for (let i = 0; i < 20; i++) {
  material = new THREE.MeshStandardMaterial({
    color: `rgb(
				${50 + Math.floor(Math.random() * 205)}
			)`,
  });
  mesh.name = `box-${i}`;
  // mesh에 이름 생성
  scene.add(mesh);
  meshes.push(mesh);
}

// Controls
// 어떤 매쉬를 드래그할것인지 - 첫번째 매개변수
const controls = new DragControls(meshes, camera, renderer.domElement);

controls.addEventListener("dragstart", (e) => {
  console.log(e.object.name);
});
```

### 7. 마인크래프트 스타일 컨트롤

- pointer lock control에 이동키 추가해보기
- wasd
