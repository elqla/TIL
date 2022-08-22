[Installation - Material UI](https://mui.com/material-ui/getting-started/installation/)

[TOC]

## INSTALL

```bash
npm install @mui/material @emotion/react @emotion/styled
```

## ICON

```jsx
import React from "react";
import AdbIcon from '@mui/icons-material/Adb';

function App() {
  return <div>
    <AdbIcon color="primary" fontSize="large"/>
  </div>
}

export default App;
```

## FONT

https://kbwplace.tistory.com/112

https://mui.com/material-ui/customization/typography/

```bash
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Typography from '@mui/material/Typography';

const theme = createTheme({
  typography: {
    htmlFontSize: 10,
    fontFamily: "sans-serif"
  },
});

export default function FontSizeTheme() {
  return (
    <ThemeProvider theme={theme}>
      <Typography>body1</Typography>
    </ThemeProvider>
  );
}
```

## 간단한 사용법

### button

```bash
import Button from '@mui/material/Button';

function App() {
  return <Button variant="contained">Hello World</Button>;
}
```

### grid

```bash
import Grid from '@mui/material/Grid';
function App() {
  return   <Grid container spacing={2}>
  <Grid item xs={8}>
    <Item>xs=8</Item>
  </Grid>
  <Grid item xs={4}>
    <Item>xs=4</Item>
  </Grid>
</Grid>
}
//12컬럼을 기준으로 나눔
```