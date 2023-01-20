[TOC]

## 1. Array

### pb1. Array.fill관련 ERROR

```js const gett = () => {
    const peoplesss = [];
    for (let i = 0; i < 30; i++) {
      const people: string[][] = new Array(5).fill([]);
      data.forEach((da) => {
        people[da.peoplenumber[i] - 1].push(da.name);
      });
      peoplesss.push(people);
    }
    return peoplesss;
  };
```

-> Array(5).fill([])로 배열을 만든결과 같은 주소를 가진 배열이 생성되었다.
당연히 모든 데이터가 people로 들어감

Sl. 배열 만들어주기

```js
//map으로 각 자리 idx에 해당되는 값이 할당됨, 즉 각각의 배열이 생성된다.
Array(5)
  .fill("")
  .map(() => []);

Array.from({ length: 5 }, () => []);
```
