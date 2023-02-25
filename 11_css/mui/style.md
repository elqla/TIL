**[MUI약어](# https://mui.com/system/properties/)**

## react inline style(랜더링 될 때마다 style 계산)

- 성능, 재사용 X

```react
<div style={{ width: 100, height: 100 }}>
```

## Mui sx (styled-component, css유틸기능 추가)

- 재사용성 취약
- https://mui.com/system/basics/#the-sx-prop

```react
<Box sx={{ width: 100, height: 100 }}>Hello Box</Box>
```

## mui  컴포넌트 재정의

```react
const MyButton = styled(Button)`
...
`;
```

```react
const Div = styled('div')({
	height: '100vh',
	width: '100vw',
	display: 'flex',
	flexDirection: 'column',
	justifyItems: 'center',
	justifyContent: 'center',
})
const StyledTypography = styled(Typography)({
  fontFamily: 'malgunbd !important',
	fontSize: 'var(--font-title-size)',
	letterSpacing: 'var(--font-title-letter-spacing)',
  color: '#000000',
})

```



## props  사용해서 재정의

```react
<SetAvatar si={12} value={i}>
	<img src={consultants[i].imageUrl} alt='MyAvatar' />
</SetAvatar>


const SetAvatar = styled(Avatar)((props) => ({
  backgroundColor: "skyblue",
  width: `${props.si * 10}px`,
  height: `${props.si * 10}px`,
  img: {
    backgroundColor: 'white',
    borderRadius: "100%",
    width: `${props.si * 9}px`,
    height: `${props.si * 9}px`,
  },
}))
```



## Box

- css 유틸을 필요로 하는  wrapper 컴포넌트 역할

  



```
vh 와 vw 는 열려있는 화면 전체의 상대길이이기 때문에 스크롤바를 포함한 길이를 반환합니다!
반면에 % 는 창이 중심이 아닌, %를 쓰고 있는 요소의 부모 요소의 길이에 맞게 반환합니다.
```

출처: https://programming119.tistory.com/93 [개발자 아저씨들 힘을모아:티스토리]



---

[참고]

[Mui Box와 div의 차이](# https://velog.io/@dishate/Mui-Box%EC%99%80-div-Mui-sx%EC%99%80-React-style-styled)
[](#)