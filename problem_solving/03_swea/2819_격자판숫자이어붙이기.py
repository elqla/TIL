def dfs(ci, cj, n, num):
    if n==6:  # n = 이동하는 횟수
        sset.add(num)
        return
    for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<4 and 0<=nj<4:
            dfs(ni, nj, n+1, num*10+arr[ni][nj])

t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    sset = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, arr[i][j])

    # 서로다른 일곱자리수들의 개수
    print(f'#{tc} {len(sset)}')



'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''