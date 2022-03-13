### 스택(stack)

> 물건을 쌓아 올린듯 자료를 쌓아 올린 형태의 자료구조 (접시 쌓기)

`datastructure`

- 선형구조를 갖는다 (자료간의 관계가 1:1)
  cf) 비선형구조: 자료간의 관계가 1:N
- 가장 마지막에 들어간 것이, 가장 처음에 나온다(후입선출)
- top: 스택의 가장 위에 있는 위치를 저장하는 데이터 (pop 등 여기서 일어남)
- size: 스택의 크기 저장하는 데이터
- items: 스택에 담길 데이터를 저장할 데이터구조

`연산`

- CreateStack: 스택을 생성하는 연산 , size 필요
- push: 삽입: 저장소에 자료 저장
- pop: 삭제: 저장소에서 자료를 꺼냄(제거하며 반환) (역순으로)
- .peek : top에 있는 item(원소)를 반환하는 연산
- .isEmpty : 스택이 공백인지 T/F
- .isFull: 스택이 차있는지 T/F



`push`

```python
def push(item):
    s.append(item)
 #마지막에 저장된거부터 꺼낼수 있는 구조인가?
----------------------------------------------------------
stack = []
stack.append(10)
stack.append(20)
print(stack.pop()) #pop(-1)
print(stack.pop())
#20
#10
#append, pop 은 느림
```

```python
def push(item, size):#넘치면 안됨
    global top     #리스트의 경우 global을 안써도 쓸 수 있음
    top += 1
    if top == size:  #일치하면, idx 벗어남(size: 1~, top: 0~)
        print('overflow')
    else:
        stack[top] = item
size = 10      #크기가 정해진 스택을 만들어 사용하기
stack = [0]*size
top = -1
---------------------------------------------------------------
push(10, size)
top += 1  		#push(20)  가 필요한 부분에 top +=1
stack[top] = 20 #20을 변수에 저장해 !  ##함수 호출도 안해서 속도도 빠름.
```

- append, pop은 조금 느림
- 크기가 정해진 배열에서 넣었다 , 빼는게 더 빠르다 !

`pop`

```python
def pop():
    if len(s) == 0: #underflow
        return 
    else:
        return s.pop(-1)  #마지막꺼 꺼내서 돌려줌
```

```python
def pop():
    global top
    if top == -1:  #없네?
        print('underflow')
        return 0
    else:
        top -= 1  #있으면 top -=1 pop  할거니까
        return stack[top+1]  #-=1된(pop) 자리 리턴
print(pop())
--------------------------------------------------------
if top >-1:   #pop()
    top -=1 #탑하나 감소시키고			  print(stack[top])
    print(stack[top+1])  #그냥 꺼내면 됨   top -=1 
------------------------------------------------------
---#자주쓰임
while top>=0:   #pop()
    n = stack[top]
    top -=1
```

---

`괄호검사`

![](stack_%EC%9E%AC%EA%B7%80_dp.assets/image.png)

```python
왼쪽괄호 push
오른쪽괄호 나오면 pop을해서 비교 
#짝이 많지 않거나, 수식이 있는데 스택이 비어서 비교할수 없거나, 끝났는데 스택에 수식이 남아있으면 오류,
```

---

`function call`

![image-20220221144107318](stack_%EC%9E%AC%EA%B7%80_dp.assets/image-20220221144107318.png)

> 함수 끝났을때 돌아올 곳의 정보도 같이 저장
>
> 함수 호출이 많으면 오래걸림, 적절한 함수 호출깊이 유지하기(깊으면, 그만큼 호출이 많아짐)
>
> 그리고 이렇게 함수를 묶어서 만들면 관리가 힘듦.
>
> 따라서, 함수를 적당히 나눠놓는게 더 좋음 !

---

## 재귀호출

```python
# factorial
n! = n x (n-1)!
		(n-1)! = (n-1) x (n-2)!
...
2! = 2x1!
1! = 1
```

![image-20220221145953707](stack_%EC%9E%AC%EA%B7%80_dp.assets/image-20220221145953707.png)

- 호출될때마다 메모리 영역이 분리됨

  ```python
  fact(n):
      if n==1:
          return 1
      else:
          return n*fact(n-1)
  ```

  ```python
  4-a
   -b..  fact(a)
   --------4
  4 | n fact(n)
  	  fact(n-1)    4*6 = 24
  ---------3
  3 | n fact(n)
  	  fact(n-1)    3*2
  ---------2
  2 | n fact(n)
  	 fact(n-1)     2*1
  --------1
  1 | n fact(n) ____ 거꾸로 올라감
  ```

  

```python
#피보나치
F0 = 0
F1 = 1
Fi = F(i-1) + F(i-2) for i >= 2
```

```python
#피보나치 재귀
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

- 보통의 재귀는 f(i, N)  #(현재, 목표)  이렇게 구성 !

```python
#일반 재귀 연습
def f(i, N):
    if i == N:
        return
    else:
        B[i] = A[i]
        f(i+1, N)

A = [10, 20, 30]
B = [0]*3
f(0, 3)
print(B)
```

## Memoization

- 동일한 계산을 반복해야 할 때, <u>이전에 계산한 값을 메모리에 저장</u>함
- 동일한 계산의 반복 수행을 제거
- 프로그램 실행 속도를 빠르게 하는 기술이다. (동적 계획법의 핵심이 되는 기술)

```python
#memo를 위한 배열 할당, 모두 0으로 초기화
#memo[0] 을 0으로 memo[1]은 1로 초기화한다.

def fibo1(n):
    global memo
    if n>=2 and len(memo)<=n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]
memo = [0, 1] #미리 저장해 두기
```

```python
0 |memo0
1 |memo1
len(memo) == 2:
    n = 2
    fibo(n-1) => fibo(n) == 1: => memo1
        fibo(n-2) => memo0 => 0
        # 따라서, 0+1
1 |memo2
```

```python
#append말고 크기 정해진 곳에 넣는법
def fibo(n):
    if n >= 2 and memo[n] == 0:  #2보다 작으면 0, 1 은 그냥 return 할수있어서
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

N = 10
memo = [0]*(N+1) #0~10
memo[0] = 0  #따로 빼봄
memo[1] = 1  #정의
print(fibo(N)) #55
print(memo)    #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

---

## DP(dynamic programming)

- 동적계획알고리즘은 그리디알고리즘과 같이 최적화 문제를 해결하는 알고리즘

  ![image-20220221154550654](stack_%EC%9E%AC%EA%B7%80_dp.assets/image-20220221154550654.png)

  

```python
#반복문으로 만들면 함수 호출 복귀 시간이 안걸림 ! (재귀보다 빠름)
for i :2->n
    fibo(i) = fibo[i-1] + fibo[i-2]
```

```python
N = 10
fibo = [0] *(N+1)
fibo[0] = [0]
fibo[1] = 1
for i in range(2, N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

```python
def fibo2(n):
    f = [0, 1]
    for i in range(2, n+1):
        f. append(f[i-1] + f[i-2])
    return f[n]
```

- DP 구현 방식
  - recursive : fib1()
  - iterable : fib2()
  - memorization 재귀에 사용 < 반복구조로 dp구현 효율 !

---

```python
class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1 				#(idx가 아닌 것으로 지정/ none 가능)
        self.items = [None] * size   #[idx]
        
    def is_empty(self):
        return True if (self.top == -1) else False #top이 -1일때, empty상태
    
    def is_full(self):
        return True if (self.size -1 == self.top) else False #또는 top+1
    				  #idx 1부터 시작    0~부터 시작
	def push(self, data):
        if self.is_full():         #가득차있으면 push 못함
            raise Exception('stack is full')
        else:
            self.top += 1
            self.items[self.top] = data
            
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            value = self.items[self.top] #값을 가져온 다음에
            self.items[self.top] = None #지워줌 /실은 그냥 [-1]해줄수도..
            self.top -= 1 #top한칸 내려줌
            return value
        
    def peek(self):
        if self.is_empty():
            raise Exception('stack is empty')
        else:
            value = self.items[self.top] # value = self.items[-1] #값을 가져온 다음에 
            return value #반환해줌
        
    def __str__(self):
        result = '\n-----'
        for item in self.items:
            if item is None:
                result = f'\n|   |' + result
            else:
                result = f'\n| {item} |' + result
        return result
    
my_stack = Stack(5)
my_stack.push(1)
my_stack.push(2)
my_stack.pop() #1만 남아있겠지
print(my_stack)
print(my_stack.size)
print(my_stack.is_empty())
#stack = []
#stack.append()
#stack.pop()
#stack[-1]
```

---

`연결리스트를 이용한 스택 ADT`

```python
#연결리스트를 담을 node class
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
        # 노드의 값, item
        # 다음 노드를 가리키는 포인터 next
class Stack:

    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)
    # 연결리스트에 요소를 추가하면서, 가장 마지막 값을 next로 지정하고
    # 포인터인 last가장 마지막으로 이동시킨다.


    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for _ in range(5):
    print(stack.pop())
```

