[TOC]

### 1. 위치이동

- position

```js
var origin = new THREE.Vector3(0, 0, 0); // 원점
var meshPosition = mesh.position; // 메쉬의 위치 (Vector3 인스턴스로 가정)
var distance = origin.distanceTo(meshPosition); // 원점에서 메쉬의 위치까지의 거리 계산
```

```js
function draw() {
  const delta = clock.getDelta();

  // mesh.position.y = 2;
  mesh.position.set(-1, 0, 0);

  // console.log( mesh.position.length() );
  // console.log( mesh.position.distanceTo(new THREE.Vector3(1, 2, 0)) );
  // console.log( mesh.position.distanceTo(camera.position) );

  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}
```

### 2. 크기조정

- scale

```js
// mesh.scale.x = 2;
// mesh.scale.y = 0.5;
mesh.scale.set(0.5, 1, 2);
```

### 3. 회전

- rotation

```js
// mesh.rotation.y = 0.5;
// reorder: 축을 변경하는 코드, 그냥 쓰면 축이 안바뀌고 로테이션 됨.
mesh.rotation.reorder("YXZ");
mesh.rotation.y = THREE.MathUtils.degToRad(45);
mesh.rotation.x = THREE.MathUtils.degToRad(20);
function draw() {
  const delta = clock.getDelta();
  // 45도를 돌리고 싶을때
  // mesh.rotation.x = THREE.MathUtils.degToRad(45);
  // mesh.rotation.x = Math.PI / 4;  //라디언값 Math.PI === 180' (3.14....)
  // mesh.rotation.x = 1;
  // mesh.rotation.z += delta;

  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}
```

### 4. 그룹 만들기

-

```js
// Mesh - 같은 메쉬라면 계속 재사용 가능
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial({
  color: "hotpink",
});

// 태양
const group1 = new THREE.Group();
const box1 = new THREE.Mesh(geometry, material);

// 지구
const group2 = new THREE.Group();
// const box2 = new THREE.Mesh(geometry, material);
const box2 = box1.clone();
box2.scale.set(0.3, 0.3, 0.3);
group2.position.x = 2;

// 달
// const group3 = new THREE.Object3D();
const group3 = new THREE.Group();
const box3 = box2.clone();
box3.scale.set(0.15, 0.15, 0.15);
box3.position.x = 0.5;

group3.add(box3);
group2.add(box2, group3);
group1.add(box1, group2);
scene.add(group1);

// // AxesHelper
// const axesHelper = new THREE.AxesHelper(3);
// scene.add(axesHelper);

// Dat GUI
const gui = new dat.GUI();
gui.add(camera.position, "x", -5, 5, 0.1).name("카메라 X");
gui.add(camera.position, "y", -5, 5, 0.1).name("카메라 Y");
gui.add(camera.position, "z", 2, 10, 0.1).name("카메라 Z");

// 그리기
const clock = new THREE.Clock();

function draw() {
  const delta = clock.getDelta();

  group1.rotation.y += delta;
  group2.rotation.y += delta;
  group3.rotation.y += delta;

  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}
```
