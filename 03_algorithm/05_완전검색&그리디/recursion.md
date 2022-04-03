```python
#가장 기본적인 구조
def f(i, N):
    if i==N:
        return
    else:
        f(i+1, N)
f(0, 3) -> f(1, 3) -> f(2, 3) -> f(3, 3) 3==3 return
# 호출할때마다, 새로운 메모리를 가지기 때문에
# 구조가 동일한 다른 함수를 가진다고 생각!

# return 후 , 함수 내부에서 생성한 로컬/매개변수는 메모리에서 사라짐
# 함수의 로컬/매개변수는 그 함수의 실행시간 동안만 존재 ! 따라서 펑 펑 퍼.ㅇ....
# 전역변수는 살아있음
```

```python
# recursion 1
def f(i, N):
    if i==N:
        return
    else:
        B[i] = A[i]   #else문 ~ 재귀호출 사이/ 재귀에서 할일을 넣는 위치(기본적으로)
        f(i+1, N)

N = 3
A = [10, 20, 30]
B = [0]*N
f(0, N)
print(B)
```

```python
# recursion 2
# 결정된 리턴값을 이전 단계에 전달
def f(i, N, v): #idx, 배열의 크기, 찾을 값
    if i==N:    # 배열을 벗어난 경우, 검색실패
        return -1
    elif A[i]==v:
        return 1
    else:   # 배열을 벗어나지 않고 검색 실패한 경우
        return f(i+1, N, v)     # 리턴값을 다시 리턴  /recur1에선 그냥 쭉 들어갔다 나왔는데 여기선 '리턴 값을'전달하는 구조임 !

A = [7,2,5,4,1,3]
N = len(A)
v = 9
print(f(0, N, v))  # 배열 A에 v가 있으면 1, 없으면 -1 리턴
```

```python
# recursion 3 중복순열
# def f(i, N): #  A[i]에 0 또는 1을 채우는 함수
#     if i==N:    # A가 채워진 경우
#         print(A)
#     else:
#         A[i] = 0
#         f(i+1, N)
#         A[i] = 1
#         f(i+1, N)
#     return
def f(i, N): #  A[i]에 0 또는 1을 채우는 함수  # 재귀호출의 단계를 결정하는 부분
    if i==N:    # A가 채워진 경우
        print(A)
    else:
        for j in range(2):  # for문의 크기가 갈림길의 개수에 따라 다르게 표현된다.(dfs) #######
            A[i] = j
            f(i+1, N)
    return

N = 3
A = [0]*N
f(0, N)
```

```python
# recursion 4
# 1,2,3을 증복사용해 3자리수 만들기
def f(i, N):
    if i==N:
        print(A)
    else:
        for j in range(1, 4):   # 트리 간선세개로 시작
            A[i] = j
            f(i+1, N)
    return

N = 3
A = [0]*N
f(0, N)
```

```python
# recursion 5
# 1~K (K>=3) 을 중복사용해 N자리수 만들기
def f(i, N, K):		# n까지의 깊이, 3자리면 3만큼만
    if i==N:
        print(A)
    else:
        for j in range(1, K+1):  #1 ..~k까지의 가림길
            A[i] = j
            f(i+1, N, K)
    return

N = 3
K = 5
A = [0]*N
f(0, N, K)
```

```python
# recursion 6
# if v 를 찾으면 탐색 중단
# dfs구조라고 가정하고,,(트리) 그 구조에서 아까 2번에선, 그냥 한 배열이였지만
# 지금은 트리구조라서,조금 조건을 다르게 쓸 것


# 1~K (K>=3) 을 중복사용해 N자리수 만들기(3)자리수
# v값을 만들 수 있으면 탐색 중단하고/리턴

def f(i, N, K, v):
    if i==N:
        s = A[0]*100+A[1]*10+A[2]
        print(s)
        if s==v:
            return 1      # 같을때, return값을 받고
        else:
            return 0
    else:
        for j in range(1, K+1):
            A[i] = j
            if f(i+1, N, K, v):  # 다음 단계에도 지금 값 찾았다고 알려줘야 하기 때문에// if f함수에 값이 있으면, 
                return 1 #return 1
        return 0  #for문을 다 돌았는데도 못찾은 경우 

N = 3
K = 5
A = [0]*N
v = 125
print(f(0, N, K, v))  #return 값 바로 받음
```

```python
# recursion 7
# 백트래킹
# A의 부분집합중 합이 K인 부분집합의 개수 구하기
def f(i, N, s, K):  # s: i-1원소까지 고려된 부분집합의 합
    global cnt
    if i==N:
        if s==K: ##여기가 중요함, 여기서 for문 돌리면 시간 오래 걸림
            cnt += 1
    else:
        f(i+1, N, s+A[i], K) # A[i]포함
        f(i+1, N, s, K)                      #(마지막값 두갈래에서, 포함 미포함 고려하여 결정)

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
K = 55
cnt = 0
f(0, N, 0, K)  #0번부터, 개수는 n, 0번원소를 고려하기 전까지의 합은 0, 
print(cnt)
```

