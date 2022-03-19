\#\#\#



### k진법

```python
lst = []
a = 1812
k = 2

while a >= k:
    m = a // k  
    n = a % k  
    lst.append(n)
    a = m 
lst.append(a)
lst = lst[::-1]
print(lst)


# [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0]
```

```python
K진법
abcd
a x k^3
b x k^2
c x k^1
d X k^0
```

```python
2|10
2|5 ---0
2|2 ---1
2|1 ---0
2|0 ---1  

10은 2진수로 [1010(2)]


#코드로 표현시
2|10
2|5 ---0  #나머지 값을 차례로 append해주고
2|2 ---1
  1 ---0    
a =1   #k진수보다 작아 나눌수 없는 '마지막 몫'을 마지막에 append
```



### float->isclose

- 부동소수점

  - 컴퓨터는 실수를,  2진수(비트)로 숫자를 표현함
  - 따라서, floating point rounding error발생

  - ```python
    10***100/3
    -> 3.33333
    ```

  - ```python
    3.14-3.02 == 0.12  #0.1200000000000001
    -> False
    ```

- 매우 작은 수보다 작은지 확인, math 모듈 활용

```python
a = 3.14-3.02
b = 0.12


1. 임의의 작은수
abs(a-b) <=1e-10 (0.0000000001)
>True

2. machine epslion
import sys
print(abs(a-b) <= sys.float_info.epsilon)
print(sys.float_info.epsilon)
>True
>2.22.....e-16

3. python3.5이상
import math
math.isclose(a, b)
>True
```



### 올림, 내림, 버림 , 반올림

```python
1. 올림
math.ceil(12.2)
>13

2. 내림
math.floor(12.6)
>12

3. 버림
math.trunc(12.6)
>12

4. 반올림
round(0.4555555, 2)
>0.45  #자리수대로 표현

round(1.77777)
>2

round(12345, -1)
>12340 #정수에도 표현 가능
```



```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    q = N**(1/3)
    q = int(q)
    for i in range(2):
        if N == (q+i)**3:
            print(f'#{tc} {q+i}')
            break
    else:
        print(f'#{tc} -1')
```

