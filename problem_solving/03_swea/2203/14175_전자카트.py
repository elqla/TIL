# sw_14175_전자카트

def perm(idx, n, res):
    if idx == n-1:
        res = [0]+res+[0]
        lst.append(res)
        return
    for i in range(1, n): # 인덱스 맞추기
        if i not in res:
            res.append(i)
            perm(idx+1, n, res)
            res.pop()

t = int(input())
for tc in range(1, t+1):
    N = int(input())  # 4  (0, 1, 2, 3)
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [] # 순열 담을 리스트
    perm(0, N, [])
    # idx, 뽑을 개수, , res

    mn = 999999999
    for l in lst:
        s = 0
        for i in range(len(l)-1):
            start, end = l[i], l[i+1]
            s += arr[start][end]

        if mn>s:
            mn = s

    print(f'#{tc} {mn}')

'''
3
3
0 18 34
48 0 55
18 7 0

'''