## 패턴 매칭

### 고지식한 패턴 검색 알고리즘  

- 인덱스연산연습하기

<img src="string-%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4.assets/image-20220216110559698.png" alt="image-20220216110559698" style="zoom: 50%;" />

```python
t   (안에 TTA가 있는가?) TTT(달라서 한칸 욺겨서 TT부터 시작)  i
p   TTA(찾아야할 패턴을지정)							j

for i: 0->N-M (N:텍스트의 길이 M:패턴의 길이)
	for j: 0->M-1(pattern의 인덱스)
		t[i+j] p[j] 비교  /같으면 for문이 계속 돌 것임
         #i는 인덱스 위치 지정 + j는 패턴위치 지정 따라서, text에서 p[j]와 같이 돌면서 비교!
    j == M 이 되서 패턴이 끝나면 찾은거고, 실패하면 i+1부터 해야하는거고!
    t[i+j] p[j] 반복 수행
```

<img src="string-%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4.assets/image-20220216111440173.png" alt="image-20220216111440173" style="zoom:50%;" />

<img src="string-%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4.assets/image-20220216111609252.png" alt="image-20220216111609252" style="zoom:50%;" />



```python
t = 'This is a book~!' #전체 텍스트
p = 'is'  #찾을 패턴

N = len(t)  #전체 텍스트의 길이 ()
M = len(p)  #찾을 패턴의 길이 ()
#언제나 i가 한칸씩 이동함. 비교 시작시,  다시 back 해줌 !

def bruteForce(p, t):
    i = 0  #시작점은 처음이기 때문에 0으로 초기화
    j = 0
    while j < M and i < N:
        if t[i] != p[j]: #실패했을때만 되돌리는 구조를 씀
            i = i-j #이전 시작점///의 다음(+1)시작점으로 돌아감
            j = -1  # 불일치 시, 0으로 만들어줘야 하는데 일치할때 1을 더하니까 0 대신 -1 사용 함
        i = i + 1	#이전 시작점/의 다음(+1)을 시작점으로
        j = j + 1  #일치할때 1을 더해줌
    if j == M: return i - M #검색성공  패턴시작위치를 돌려줌 !
    else:
        return -1  #검색실패
a = bruteForce(p, t)
print(a) #검색 성공 !... pattern이 등장한 text의 idx return
---
#2
def bruteForce(p, t):
    n = len(t)
    m = len(p)
    
    for i in range(n - m + 1): #패턴의 길이만큼 빼주고, idx를 맞춰야 해서 +1
        for j in range(m):		#맞으면 계속 이 for문을 돌아 else로 탈출 !
            if t[i+j] != p[j]:    #시작위치에서 몇칸 이동?? (i+j)  틀렸으면 멈추고!
                break         #i+1 은 자동으로 되고, m = 0으로 해줘야되는데 
                			#break를 통해 가까운 반복문으로 올라감
        else:                #새로운 for문이 시작되기 때문에 초기화가 됨 m = 0  //while은 초기화 안됨
            return 1   #성공  # else의 동작 :: for문에서 break가 발생하지 않을시 동작함
       						
	return 0 	#실패

-----------------------------------
		else:
        	return i #성공 (근데 첨에 성공하면 0 이 나올수 있어서)
    return -1   #실패값을 바꿔주면 되겠지
--------------------------------
#3
	lst = []
    for i in range(n - m + 1):
        for j in range(m):
            if t[i+j] != p[j]:    
                break     
        else:               
            lst.append(i)		#idx 위치 반환
                  #브레이크는 하나밖에 못 빠져나옴, 그래서 함수로 감싼 후. 성공하면 리턴
	return lst 	#실패

---
#??
if []: #false
    
while[]:
    print(lst.pop())

-------
    for i in range(n - m + 1):
        for j in range(m):
            if t[i+j] != p[j]:    
                break     
        else:               
            success = 1			
            break         #브레이크는 하나밖에 못 빠져나옴, 그래서 함수로 감싼 후.  성공했어 ? 리턴@
	return 0 	#실패
-----------------------------------------------------
    for i: 0->N-M (N:텍스트의 길이 M:패턴의 길이)
	for j: 0->M-1 (M개면 M-1까지)
        while j < M
		t[i+j] p[j] 비교
---------------------------------------------
#i 고정, 한칸이동할때 j칸 이동해
def bruteForce(p, t):
    i = 0  #시작점은 처음이기 때문에 0으로 초기화
    j = 0
    while i + j <len(t) and j < len(p): #비교할게 없고, 
        if t[i+j] != p[j]:
            i += 1
            j = 0
        else:          #같다면
            j += 1   #j 의 시작점을 +1
        if j == len(p):
            return 1 #성공을 return
    return -1 #while 다 돌았지만 실패
```

- 시간복잡도
  - O(MN) : 텍스트의 모든 위치에서 패턴을 비교해야 함
  - 전체 길이 M을 단어의 횟수 N만큼 해주어야 해서!



---

---

```python
# T : target / P : pattern


def pre_process(P):
    from collections import defaultdict

    M = len(P)    

    # skip 배열 대신 딕셔너리
    PI = defaultdict(int)

    # 실 사용은 M - value로 할 예정.
    for i in range(M-1):
        PI[P[i]] = 1 + i
    return PI


def boyer_moore(T, P, PI):

    N = len(T)
    M = len(P)

    i = 0
    # 실패할 경우 -1 return
    pos = -1

    while i <= N - M:
        # skip 잘 되고있나 확인
        print(i)

        # 
        # M번째 인덱스
        j = M - 1
        k = i + M - 1

        # 비교할 j가 남아있고, text와 pattern이 같으면 1씩 줄여 왼쪽 비교
        while j >= 0 and P[j] == T[k]:
            j -= 1
            k -= 1
        # 비교 성공
        if j == -1:
            pos = i
            break
        # i를 M - value만큼 스킵
        i = i + M - PI[T[i + M - 1]]

    return pos




# Target 문자
T = "a pattern matching algorithm"

# Pattern 문자
P = "rithm"

# skip 배열을 만들어줌
PI = pre_process(P)
print(PI)

# target, pattern, skip배열을 인자로 넘김
pos = boyer_moore(T, P, PI)
print(pos)
```



```python
# T : target / P : pattern

def pre_process(P):

    M = len(P)
    lps = [0] * len(P)
    
    j = 0

    for i in range(1,M):
        if P[i] == P[j]:
            lps[i] = j + 1
            j += 1
        else:
            j = 0
            if P[i] == P[j]:
                lps[i] = j + 1
                j += 1  

    return lps


def KMP(T, P, lps):

    N = len(T)
    M = len(P)

    i, j = 0, 0
    pos = -1
    while i < N:
        if P[j] == T[i]:
            i += 1
            j += 1
        else:
            if j!= 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:
            pos = i - j
            break

    return pos

T = 'abcdabeeababcdabcef'
P = 'abcdabcef'


N = len(T)
M = len(P)
lps = pre_process(P)
print(lps)

pos = KMP(T, P, lps)
print(pos)
```

