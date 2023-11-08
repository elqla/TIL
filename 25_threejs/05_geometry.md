[TOC]

### 1. 여러가지 Geometry

[geometry_threejs](https://threejs.org/docs/index.html?q=geometry#api/en/geometries/BoxGeometry)

```js
// 줌인, 줌아웃 등 궤도 컨트롤 - 카메라 관련
const controls = new OrbitControls(camera, renderer.domElement); // 캔버스 객체 (renderer.domElement)

const material = new THREE.MeshStandardMaterial({
  wireframe: true, // 뼈대만 보임
  side: THREE.DoubleSide, // 반대편 면 생성 (기존-카메라로 객체 안에서 보면 한면밖에 안보임)
});
```

### 2. Geometry 형태 조작하기 1

- segment를 나눈다.

[sphere_geometry](https://threejs.org/docs/index.html?q=geometry#api/en/geometries/SphereGeometry)

```js
// Mesh
const geometry = new THREE.SphereGeometry(5, 64, 64);
// const geometry = new THREE.PlaneGeometry(10, 10, 32, 32);
const material = new THREE.MeshStandardMaterial({
  color: "orangered",
  side: THREE.DoubleSide,
  flatShading: true,
});
console.log(geometry.attributes.position.array); // Array => x, y, z 순서대로 나옴 (점개수 * 3)
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);
```

### 3. Geometry 형태 조작하기 2

```js
const positionArray = geometry.attributes.position.array;
const randomArray = [];
for (let i = 0; i < positionArray.length; i += 3) {
  // 정점(Vertex) 한 개의 x, y, z 좌표를 랜덤으로 조정
  // positionArray[i] = positionArray[i] + (Math.random() - 0.5) * 0.2;
  positionArray[i] += (Math.random() - 0.5) * 0.2; // 0~1사이의 숫자 중 랜덤 (값이 커져서 무조건 오른쪽으로 가므로, -0.5를 해줘 분포시킴)
  positionArray[i + 1] += (Math.random() - 0.5) * 0.2;
  positionArray[i + 2] += (Math.random() - 0.5) * 0.2;

  randomArray[i] = (Math.random() - 0.5) * 0.2;
  randomArray[i + 1] = (Math.random() - 0.5) * 0.2;
  randomArray[i + 2] = (Math.random() - 0.5) * 0.2;
}
```

### 4. Geometry 형태 조작하기 3, 4

- animtaion 적용

```js
const clock = new THREE.Clock();

function draw() {
  const time = clock.getElapsedTime() * 3; // 경과 시간 이용

  for (let i = 0; i < positionArray.length; i += 3) {
    // sin, cos 사용하면 큰 파형을 만들 수 있음.
    // 각도의 변화가 있어야 값이 변하므로, time
    // positionArray[i] += Math.sin(time) * 0.002
    positionArray[i] += Math.sin(time + randomArray[i] * 100) * 0.001;
    positionArray[i + 1] += Math.sin(time + randomArray[i + 1] * 100) * 0.001;
    positionArray[i + 2] += Math.sin(time + randomArray[i + 2] * 100) * 0.001;
  }
  // 계속 없데이트 하려면 true 속성 줘야함.
  geometry.attributes.position.needsUpdate = true;

  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}

draw();
```
