### 1. Light 사용법

- ambientLight: 은은함, 단독으로 잘 안씀, 위치속성 없음.

- DirectionalLight: 태양광처럼 전체적으로 뿌려짐.

```js
// (색상, 빛의 강도)
const ambientLight = new THREE.AmbientLight("white", 0.5);
scene.add(ambientLight);

const light = new THREE.DirectionalLight("red", 0.5);
// light.position.x = -3;
light.position.y = 3;
scene.add(light);

const lightHelper = new THREE.DirectionalLightHelper(light);
scene.add(lightHelper);

// Dat GUI
const gui = new dat.GUI();
gui.add(light.position, "x", -5, 5);
gui.add(light.position, "y", -5, 5);
gui.add(light.position, "z", -5, 5);
```

### 2. Light 애니메이션

```js
const clock = new THREE.Clock();

function draw() {
  // delta는 draw함수가 실행되는 시간 간격
  // const time = clock.getDelta()
  // elapsedtime은 계속 늘어나는 시간 반영
  const time = clock.getElapsedTime();

  // light.position.x = Math.cos(time) * 5;
  // light.position.z = Math.sin(time) * 5;

  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}
```

### 3. 그림자 처리

- castshadow: 영향을 줌. 다른곳에 그림자 생기도록
- receiveShadow: 영향을 받음, 그림자가 생김

```js
// 그림자 설정
renderer.shadowMap.enabled = true;
// renderer.shadowMap.type = THREE.PCFShadowMap;
// renderer.shadowMap.type = THREE.BasicShadowMap; // 깨져보임
// renderer.shadowMap.type = THREE.PCFSoftShadowMap;

light.castShadow = true;
// 그림자 화질 좋아지도록
light.shadow.mapSize.width = 1024; // 기본값 512
light.shadow.mapSize.height = 1024;
light.shadow.camera.near = 1; //
light.shadow.camera.far = 30;
// light.shadow.radius = 15; // 기본값인 THREE.PCFShadowMap에서만 적용/ 그림자 부드럽게

// 그림자 설정
plane.receiveShadow = true;
box.castShadow = true;
box.receiveShadow = true;
sphere.castShadow = true;
sphere.receiveShadow = true;
```

### 4. PointLight

- 전구

```js
const light = new THREE.PointLight("white", 1, 100, 2);
const lightHelper = new THREE.PointLightHelper(light);
```

### 5. SpotLight

- 원뿔모양이라 각도가 있음.

```js
const light = new THREE.SpotLight("white", 1, 30, Math.PI / 6);
```

### 6. HemisphereLight

- ambientlight처럼 은은하게 전체적으로 영향을 미침.

- 얘도 그림자가 없기때문에 light.shadow, castshadow 등 주석

```js
const light = new THREE.HemisphereLight("pink", "lime", 1);
light.position.x = -5;
light.position.y = 3;
scene.add(light);

const lightHelper = new THREE.HemisphereLightHelper(light);
```

### 7. RectAreaLight

- 사각형 판에서 빛이 뿜어져 나간다.

```js
const light = new THREE.RectAreaLight("orange", 10, 2, 2);
// light.position.x = -5;
light.position.y = 2;
light.position.z = 3;
scene.add(light);

const lightHelper = new RectAreaLightHelper(light);
scene.add(lightHelper);
```
