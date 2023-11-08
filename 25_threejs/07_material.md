### 1. MeshBasicMaterial

- 빛, 그림자 영향 안받음
- 성능 좋음

### 2. MeshLambertMaterial, MeshPhongMaterial

```js
// Mesh
const geometry = new THREE.SphereGeometry(1, 16, 16);
// MeshLambertMaterial 하이라이트, 반사광 없는 재질
const material1 = new THREE.MeshLambertMaterial({
  color: "orange",
});
// MeshPhongMaterial 하이라이트, 반사광 표현 가능
const material2 = new THREE.MeshPhongMaterial({
  color: "orange",
  shininess: 1000,
});
```

### 3. MeshStandardMaterial

- roughness, metalness 조절 가능

```js
const material2 = new THREE.MeshStandardMaterial({
  color: "orangered",
  // 거칠기
  roughness: 0.2,
  // 금속성 재질 정도
  metalness: 0.3,
});
```

### 4. 각지게 표현, flatShading

```js
const material2 = new THREE.MeshPhongMaterial({
  color: "orange",
  shininess: 1000,
  flatShading: true,
});
```

### 5. Mesh의 앞뒷면

- 면(side)

```js
const material = new THREE.MeshStandardMaterial({
  color: "orangered",
  roughness: 0.2,
  metalness: 0.3,
  // side: THREE.FrontSide
  // side: THREE.BackSide
  side: THREE.DoubleSide,
});
```

### 6. 텍스쳐 이미지 로드하기

- 3d texture

```js
// 텍스쳐 이미지 로드
const textureLoader = new THREE.TextureLoader();
// const texture = textureLoader.load('/textures/brick/Brick_Wall_019_basecolor.jpg');
const texture = textureLoader.load(
  "/textures/mcstyle/back.png",
  () => {
    console.log("로드 완료");
  },
  () => {
    console.log("로드 중");
  },
  () => {
    console.log("로드 에러");
  }
);

const material = new THREE.MeshStandardMaterial({
  // color: 'orangered',
  map: texture,
});
```

### 7. 로딩매니저(여러개의 텍스쳐 이미지)

```js
// 텍스쳐 이미지 로드
const loadingManager = new THREE.LoadingManager();
loadingManager.onStart = () => {
  console.log("로드 시작");
};
loadingManager.onProgress = (img) => {
  console.log(img + " 로드");
};
loadingManager.onLoad = () => {
  console.log("로드 완료");
};
loadingManager.onError = () => {
  console.log("에러");
};
const textureLoader = new THREE.TextureLoader(loadingManager);
const baseColorTex = textureLoader.load("/textures/brick/Brick_Wall_019_basecolor.jpg");
const material = new THREE.MeshStandardMaterial({
  map: baseColorTex,
});
```

### 8. 텍스쳐 변환

```js
const textureLoader = new THREE.TextureLoader(loadingManager);
const texture = textureLoader.load("/textures/tooncubemap/roket.jpg");

// 텍스쳐 변환
texture.wrapS = THREE.RepeatWrapping;
texture.wrapT = THREE.RepeatWrapping;

// texture.offset.x = 0.3;
// texture.offset.y = 0.3;

// texture.repeat.x = 2;
// texture.repeat.y = 2;

// texture.rotation = Math.PI * 0.25;
texture.rotation = THREE.MathUtils.degToRad(60);
texture.center.x = 0.5;
texture.center.y = 0.5;
```

### 9. 여러 이미지 텍스쳐가 적용된 큐브

```js
const textureLoader = new THREE.TextureLoader();
const rightTexture = textureLoader.load("/textures/mcstyle/right.png");
const leftTexture = textureLoader.load("/textures/mcstyle/left.png");
const topTexture = textureLoader.load("/textures/mcstyle/top.png");
const bottomTexture = textureLoader.load("/textures/mcstyle/bottom.png");
const frontTexture = textureLoader.load("/textures/mcstyle/front.png");
const backTexture = textureLoader.load("/textures/mcstyle/back.png");

const materials = [
  new THREE.MeshBasicMaterial({ map: rightTexture }),
  new THREE.MeshBasicMaterial({ map: leftTexture }),
  new THREE.MeshBasicMaterial({ map: topTexture }),
  new THREE.MeshBasicMaterial({ map: bottomTexture }),
  new THREE.MeshBasicMaterial({ map: frontTexture }),
  new THREE.MeshBasicMaterial({ map: backTexture }),
];
// 작은사이즈의 픽셀을 살리기 위함.
rightTexture.magFilter = THREE.NearestFilter;
leftTexture.magFilter = THREE.NearestFilter;
topTexture.magFilter = THREE.NearestFilter;
bottomTexture.magFilter = THREE.NearestFilter;
frontTexture.magFilter = THREE.NearestFilter;
backTexture.magFilter = THREE.NearestFilter;

const mesh = new THREE.Mesh(geometry, materials);
```

### 10. MeshTooMaterial(만화느낌)

```js
const gradientTex = textureLoader.load("/textures/gradient.png");
gradientTex.magFilter = THREE.NearestFilter;

// Mesh
const geometry = new THREE.ConeGeometry(1, 2, 128);
const material = new THREE.MeshToonMaterial({
  color: "plum",
  gradientMap: gradientTex,
});
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);
```

### 11. MeshNormalMaterial

- 면에 수직인 선: Normal (법선)
- MeshNormalMaterial은 방향에 따라 색이 변함.

```js
// Mesh
const geometry = new THREE.BoxGeometry(2, 2, 2);
// 구는 법선의 각도가 일정해서, 돌려도 색이 일정함.
// const geometry = new THREE.SphereGeometry(1, 64, 64);
const material = new THREE.MeshNormalMaterial();
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);
```

### 12. MeshMatcapMaterial

- matcap texture
- 입체감이 있는 사진을 Mesh에 적용해줌.

```js
const matcapTex = textureLoader.load("/textures/matcap/Copper_1.png");
// const geometry = new THREE.BoxGeometry(2, 2, 2);
const geometry = new THREE.ConeGeometry(1, 2, 64);
const material = new THREE.MeshMatcapMaterial({
  matcap: matcapTex,
});
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);
```

### 13. MeshStandardMaterial에 효과 더하기

```js
const baseColorTex = textureLoader.load("/textures/brick/Brick_Wall_019_basecolor.jpg");
const ambientTex = textureLoader.load("/textures/brick/Brick_Wall_019_ambientOcclusion.jpg");
const normalTex = textureLoader.load("/textures/brick/Brick_Wall_019_normal.jpg");
const roughnessTex = textureLoader.load("/textures/brick/Brick_Wall_019_roughness.jpg");
const heightTex = textureLoader.load("/textures/brick/Brick_Wall_019_height.png");

const geometry = new THREE.BoxGeometry(3, 3, 3);
// const material = new THREE.MeshBasicMaterial({
const material = new THREE.MeshStandardMaterial({
  map: baseColorTex,
  roughness: 0.3,
  metalness: 0.3,
  normalMap: normalTex,
  roughnessMap: roughnessTex,
  aoMap: ambientTex,
  aoMapIntensity: 5,
  color: "red",
});
```

### 14. EnvironmentMap

- hdr 파일 다운 후 cubemap으로 변환 (hdr to cubemap)
- https://polyhaven.com/
- https://matheowis.github.io/HDRI-to-CubeMap/

```js
// 텍스쳐 이미지 로드
const cubeTextureLoader = new THREE.CubeTextureLoader();
const envTex = cubeTextureLoader.setPath("/textures/cubemap/").load([
  // 축 기준 + - 순서
  "px.png",
  "nx.png",
  "py.png",
  "ny.png",
  "pz.png",
  "nz.png",
]);

// Mesh
const geometry = new THREE.BoxGeometry(3, 3, 3);
const material = new THREE.MeshBasicMaterial({
  // const material = new THREE.MeshStandardMaterial({
  // metalness: 2,
  // roughness: 0.1,
  envMap: envTex,
});
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);
```

### 15. SkyBox

```js
scene.background = cubeTextureLoader.setPath("/textures/cubemap/").load([
  // + - 순서
  "px.png",
  "nx.png",
  "py.png",
  "ny.png",
  "pz.png",
  "nz.png",
]);
```

### 16. Material에 Canvas 사용하기

- canvas에서 텍스쳐 만듦

```js
// CanvasTexture
const texCanvas = document.createElement("canvas");
const texContext = texCanvas.getContext("2d"); // 그림그리려면 필요함. 붓 같은 존재
texCanvas.width = 500;
texCanvas.height = 500;
const canvasTexture = new THREE.CanvasTexture(texCanvas);

// Mesh
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshBasicMaterial({
  map: canvasTexture,
});
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);

// 그리기
const clock = new THREE.Clock();

function draw() {
  const time = clock.getElapsedTime();
  // 이동하는 객체 만들수있음
  material.map.needsUpdate = true;

  texContext.fillStyle = "green"; // 붓에 물감
  texContext.fillRect(0, 0, 500, 500); // 사각형(x, y, 가로, 세로)
  texContext.fillStyle = "white";
  texContext.fillRect(time * 50, 100, 50, 50);
  texContext.font = "bold 50px sans-serif";
  texContext.fillText("1분코딩", 200, 200);

  renderer.render(scene, camera);
  renderer.setAnimationLoop(draw);
}
```
