### 회문1

```python

for i in range(N):
    for j in range(N-M+1):  #i, j라는 시작점
        for k in range(M//2):   #팰린드롬여부
            #lst[i][j] ~lst[i][j+M]
            lst[i][j+k] != lst[i][j+M-k-1]  #왼쪽 k만큼 커지고, 우측은 k만큼 줄어듦
            # 즉 , 팰린트롬을 반으로 나눈 k의 값으로
            # idx를 +k만큼, (끝에서) -k만큼 감소하면서 idx를 이동시킴
       		#i,j라는 시작점을 기준으로 회문or not체크
```

- 행에 대한 연산 하고 싶으면 자리만 바꾸기

`회문 1 활용`

```python
	def palindrome(arr, n, m):
        for i in range(n):
            for j in range(n-m+1):
                for k in range(m//2):
                    if arr[i][j+k] != arr[i][j-k+m-1]:
                        break
                else:
                    lst = arr[i][j:j + m]
                    return lst
        return []
    
    ---또는
                else:
                     lst = arr[i][j:j + m]
                     lst_str = "".join(lst)
                     return lst_str
         return ''
    
```



### 회문2

길이 M이 주어져있지가 않음

```python
M(100~0) 
for M in range(100, 1, -1):  #1전까지 ! (1은 무조건 회문)  #회문길이 100 찾고, 99 찾고..(100, 0, -1)가능
   for i in range(N):
    for j in range(N-M+1):  #M(회문의 길이)를 사용해야해서, M을 먼저 지정해줘야함
        for k in range(M//2):   #팰린드롬여부
            lst[i][j+k] != lst[i][j+M-k-1]  
            
            lst[i][j:j+M] == lst[i][j:j+M][::-1] #두개가 팰린드롬인지도 알수 있음
```

---

---

```python
word = input('단어입력')
is_palindrome = True  #회문 판별값을 저장할 변수에 true를 줌
for i in range(len(word)//2):
    if word[i] != word[-1-i]:  #-1부터니까
        is_palindrome = False
        break
print(is_palindrome)
```

```python
word == 'level'
print(word == word[::-1])
```

```python
word == 'level'
if list(word) == list(reversed(word)):
```

```python
word == 'level'
word == ''.'join'(reversed(word))
```

- pop

```python
word == [1, 3, 5, 3, 2]
while len(word)>1:
    if word.pop(0) != word.pop():
        return False
return True
```

- 리스트로 나눠담기

```python
src = list('A man,a plan, a canal - Panama!')
des = []
for val in src:
    if val.isalpha():
        des.append(val)
cnt = int(len(des)/2)

left = [des[x].lower() for x in range(0, cnt)] #cnt전까지 돌기
right = [des[-x].lower() for x in range(1, cnt+1)]  #-1 부터 -(cnt+1):(cnt의 위치) 까지

if left == right:
    print('회문')
else:
    print('낫회문')
```

---

참고자료

https://www.youtube.com/watch?v=rYMHHemvadQ







