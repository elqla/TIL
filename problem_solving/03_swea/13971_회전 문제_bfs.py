from collections import deque

t = int(input())
# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때,
# 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

for tc in range(1, t+1):
    n, m = map(int, input().split()) # n개의 수, 작업 m번
    res = ''
    q = deque()

    num_lst = input().split() # ['5527', '731', '31274']
    for i in range(n):
        q.append(num_lst[i]) # deque(['5527', '731', '31274'])
    for _ in range(m):
        f = q.popleft()
        q.append(f)  # q += f 이렇게 쓰니까 요소가 하나씩 들어감, extend('') 처럼
    res += q.popleft()

    print(f'#{tc} {res}')



'''
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907
'''





