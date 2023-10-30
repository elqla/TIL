[TOC]

### 1. Renderer - 기본 장면 만들기

- canvas

```js
const canvas = document.querySelector("#three-canvas");
// const renderer = new THREE.WebGLRenderer({ canvas: canvas });
const renderer = new THREE.WebGLRenderer({
  canvas, // canvas: canvas
  antialias: true, // 부드럽게 다듬어줌 / 성능저하 조금 O
});
renderer.setSize(window.innerWidth, window.innerHeight); // 종횡비 (aspect ratio)
```

### 2. Camera - 기본 장면 만들기

- scene (장면/무대)
- 시야각(fov): 도형의 수직각도 (눈으로 보이는 부분!)
- 종횡비(aspect): 높이/너비
- 근평면(near): 가까우면 안보이고
- 원평면(far): 먼쪽 한계

```js
const scene = new THREE.scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
// 위치 설정 해줘야함.
camera.position.x = 1;
camera.position.y = 2;
camera.position.z = 5;
scene.add(camera);
```

### 3. Mesh - 기본 장면 만들기

Geometry(모양) + material(옷) = Mesh

```js
const geometry = new THREE.BoxGeometry(1, 1, 1); //1m1m1m의 정육면체

const meterial =  new THREE.MeshBasicMaterial({
  color: 0xff0000;
})

const mesh = new THREE.Mesh(geometry,meterial)

scene.add(mesh)
//그리기
renderer.render(scene,camera)
```

### 4. Orthographic Camera - 직교 카메라

near ~ far : 절두체
Orthographic projection의 경우 직육면체로 절두체가 생김 (바로 직각에서 봄)

- camera 속성
  - camera.lookAt(0,0,0)
  - camera.zoom = 0.5 // zoomout
  - camera.updateProjcetionMatrix()

### 5. 소스코드 구조 잡기

### 6. 브라우저 창 사이즈 변경 대응

```js
funcion setSize(){
  camera.aspect = window.innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  // 변화됐으니 렌더러로 setsize해주는 것까지
  rendere.setSize(window.innerWidth, window.innerHeight);
  window.render(scene,camera)
}
window.addEventListner("resize", setSize)
```

- 고해상도로 표현해주려면, 이미지는 100px이지만, 200px로 만들여서 줄임.
- canvas도 이런 원리를 사용할 수 있음.

```js
console.log(window.devicePixelRatio); // 2 -> 픽셀 비율이 2라는 얘기 (100px -> 실제 200px을 씀)
// renderer.setPixelRatio(window.devicePixelRatio); // 실제 사이즈를 2배로 설정해줌. 보이는건 그대로.
renderer.setPixelRatio(window.devicePixelRatio > 1 ? 2 : 1);
```

### 7. 배경색, 투명도 설정

**renderer**

```js
const renderer = new THREE.WebGLRenderer({
  canvas,
  antialias: true,
  alpha: true, // 투명도 줘서 백그라운드 색 보이도록 함.
});
renderer.setClearAlpha(0.5); // 불투명도
renderer.setClearColor(0x00ff00); // 배경색, css bg로 줘도 됨
```

**scene**

- renerer가 아래 깔려 있고, 씬은 위에 덮어 씀.

```js
const scene = new THREE.Scene();
scene.background = new THREE.Color("blue");
```

### 8. 빛 (조명, Light)

- 태양이라고 생각하기
- position으로 위치 지정
- 성능에 영향 미칠 수 있음

```js
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

const light = new THREE.DirectionalLight(0xffffff, 1); // (color, 조명정도)
scene.add(light);
light.position.z = 2;
light.position.y = 2;
light.position.x = 1;
// MeshBasicMaterial은 빛에 영향을 안받음
const material = new THREE.MeshStandardMaterial({
  color: "red",
}); // standard로 바꿔줘야함.
```

### 9. 애니메이션 기본

- canvas와 마찬가지로 window.requestAnimationFrame() 사용함

1. 박스 회전시킴
2. 리페인트

```js
// 박스
const mesh = THREE.Mesh(geometry, material);
// 그리기
function draw() {
  // mesh.rotation.y += 0.1; // radian 값으로, 360도 == 2파이
  mesh.rotation.y += THREE.MathUtils.degToRad(1); //1도씩 돌림, 사용하는 화면 주사율을 따라감
  mesh.position.y += 0.01;
  if (mesh.position.y > 3) {
    mesh.position.y = 0;
  }
  renderer.render(scene, camera);
  // window.requestAnimationFrame(draw);
  renderer.setAnimationLoop(draw); // Three.js를 이용해서 AI나 VR같은 환경으로 만들땐 setAnimationLoop를 꼭 써야함.
}
draw();
```

### 10. 애니메이션 성능 보정

- 9번에 따르면, 기기별 성능에 따라 버벅일 수 있음.
- clock으로 보정
- 환경에 따라 속도가 다르진 않음. 프레임 수가 다를지언정..!

**Time**

```js
const clock = new THREE.Clock();
// 그리기
function draw() {
  // console.log(clock.getElapsedTime());
  const time = clock.getElapsedTime();
  mesh.rotation.y = time; // * 10
  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}
draw();
```

-> 문제: mesh.position.y = time 했을때 값이 애매해짐.

**Delta**

```js
const clock = new THREE.Clock();

// 그리기
function draw() {
  const delta = new THREE.getDelta();
  // 현재와 이전의 getElapsedTime의 시간차를 이용
  // getElapsedTime과 getDelta 같이 쓰지 않기.
  mesh.rotation.y += 2*delta;
  mesh.position.y =+= delta
  if(mesh.position.y > 3){
    mesh.position.y = 0;
  }
  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}
draw();
```

**Javascript Date Object**

- 계산이 Threejs와 관련없어서 canvas에서도 쓸 수 있음.
- requestAnimationFrame을 쓰는 곳이라면 같이 사용 고려

```js
let oldTime = Date.now();
// UTC기준 1970년 1월 1일 0시 0분 0초부터 현재까지 경과된 밀리초..

function draw() {
  const newTime = Date.now();// oldtime과 시간차 있을것
  const deltaTime = newTime - oldTime; // 수가 크당..
  oldTime = newTime;
  mesh.rotation.y += deltaTime * 0.005;
  mesh.position.y =+= deltaTime * 0.005;
  if(mesh.position.y > 3){
    mesh.position.y = 0;
  }
  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}
draw();
```

### 11. 안개(Fog)

```js
const meshes = [];
let mesh;
for (let i = 0; i < 10; i++) {
  mesh = new THREE.Mesh(geometry, material);
  mesh.position.x = Math.random() * 5 - 2.5;
  mesh.position.y = Math.random() * 5 - 2.5;
}
// 잘 안보이면 light position y 변경
scene.fog = new THREE.Fog("black", 3, 7); // (color, near, far)
```

### 12. 라이브러리 이용한 애니메이션

- GreenSock (npm i gsap)

```js
gsap.to(
  mesh.position, // 무엇을 ?
  {
    duration: 1, // 재생시간
    y: 2, // 이동하기 원하는 위치
    z: 3,
  }
);
```

### ETC npm, webpack 사용하지 않고 개발하기

- three.js zip파일 다운로드
- webpack을 쓸땐 js 파일 연결 안했지만 module script로 연결해줘야함.
