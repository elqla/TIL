### 1. Raycaster동작원리

- x-ray의 ray

- ray로 클릭 감지

### 2. Line으로 선 만들고 메쉬 배치

```js
// 광선을 보이게 하기 위한 geometry
const lineMaterial = new THREE.LineBasicMaterial({ color: "yellow" });
const points = [];
points.push(new THREE.Vector3(0, 0, 100));
points.push(new THREE.Vector3(0, 0, -100));
const lineGeometry = new THREE.BufferGeometry().setFromPoints(points);
const guide = new THREE.Line(lineGeometry, lineMaterial);
scene.add(guide);

const boxGeometry = new THREE.BoxGeometry(1, 1, 1);
const boxMaterial = new THREE.MeshStandardMaterial({ color: "plum" });
const boxMesh = new THREE.Mesh(boxGeometry, boxMaterial);
boxMesh.name = "box";

const torusGeometry = new THREE.TorusGeometry(2, 0.5, 16, 100);
const torusMaterial = new THREE.MeshStandardMaterial({ color: "lime" });
const torusMesh = new THREE.Mesh(torusGeometry, torusMaterial);
torusMesh.name = "torus";

scene.add(boxMesh, torusMesh);

const meshes = [boxMesh, torusMesh];

const raycaster = new THREE.Raycaster();
```

### 3. 특정 광선 지나는 메쉬 체크하기

```js
// 그리기
const clock = new THREE.Clock();

function draw() {
  // const delta = clock.getDelta();
  const time = clock.getElapsedTime();

  boxMesh.position.y = Math.sin(time) * 2;
  torusMesh.position.y = Math.cos(time) * 2;
  boxMesh.material.color.set("plum");
  torusMesh.material.color.set("lime");

  // 광선 세팅
  const origin = new THREE.Vector3(0, 0, 100);
  // const direction = new THREE.Vector3(0, 0, -1);
  const direction = new THREE.Vector3(0, 0, -100);
  // console.log(direction.length());
  direction.normalize();
  // console.log(direction.length());
  raycaster.set(origin, direction);

  // 배열의 메쉬 체크
  const intersects = raycaster.intersectObjects(meshes);
  intersects.forEach((item) => {
    // console.log(item.object.name);
    item.object.material.color.set("red");
  });
}
```

### 4. 클릭 메쉬 감지

```js
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

// 그리기
const clock = new THREE.Clock();

function draw() {
  // const delta = clock.getDelta();
  const time = clock.getElapsedTime();

  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}

function checkIntersects() {
  raycaster.setFromCamera(mouse, camera);

  const intersects = raycaster.intersectObjects(meshes);
  for (const item of intersects) {
    console.log(item.object.name);
    item.object.material.color.set("red");
    break;
  }
  // if (intersects[0]) {
  // 	intersects[0].object.material.color.set('blue');
  // }
}
// 이벤트
canvas.addEventListener("click", (e) => {
  mouse.x = (e.clientX / canvas.clientWidth) * 2 - 1;
  mouse.y = -((e.clientY / canvas.clientHeight) * 2 - 1);
  // console.log(mouse);
  checkIntersects();
});

const preventDragClick = new PreventDragClick(canvas);
```

### 5. 드래그 클릭 방지

```js
function checkIntersects() {
  if (mouseMoved) return;
  //...
}

let mouseMoved;
let clickStartTime;
let clickStartX;
let clickStartY;
canvas.addEventListner("mousedown", (e) => {
  clickStartX = e.clientX;
  clickStartY = e.clientY;
  clickStartTime = Date.now();
});
canvas.addEventListner("mouseup", (e) => {
  const xGap = Math.abs(e.clientX - clickStartX);
  const yGap = Math.abs(e.clientY - clickStartY);
  const timeGap = Date.now() - clickStartTime;
  if (xGap > 5 || yGap > 5 || timeGap > 500) {
    mouseMoved = true;
  } else {
    mouseMoved = false;
  }
});
```

### 6. 모듈화

```js
function checkIntersects() {
  console.log(preventDragClick.mouseMoved);
  if (preventDragClick.mouseMoved) return;
  //...
}

export class PreventDragClick {
  constructor(elem) {
    // this로 이 객체의 속성으로 만들어줌.
    // 밖에서 인스턴스 속성으로 접근 가능
    this.mouseMoved; // 마우스를 드래그 했는지 true/false
    let clickStartX;
    let clickStartY;
    let clickStartTime;
    elem.addEventListener("mousedown", (e) => {
      clickStartX = e.clientX;
      clickStartY = e.clientY;
      clickStartTime = Date.now();
    });
    elem.addEventListener("mouseup", (e) => {
      const xGap = Math.abs(e.clientX - clickStartX);
      const yGap = Math.abs(e.clientY - clickStartY);
      const timeGap = Date.now() - clickStartTime;

      if (xGap > 5 || yGap > 5 || timeGap > 500) {
        this.mouseMoved = true;
      } else {
        this.mouseMoved = false;
      }
    });
  }
}
```
