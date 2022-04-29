def dfs(si, sj, s):
    global mn
    if s>mn:
        return
    if si==sj==N-1:
        if s<mn:
            mn = s
        return
    for di, dj in [(1, 0), (0, 1)]: # 아래, 오른쪽
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<N:
            s = s+arr[ni][nj]
            dfs(ni, nj, s)
            s = s-arr[ni][nj]


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mn = 1e9
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {mn}')


'''
2
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
'''