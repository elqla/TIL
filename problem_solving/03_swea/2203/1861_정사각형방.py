def bfs(si, sj):
    q = []
    s = []  # 시작지점 + alpha

    q.append((si, sj))
    v[si][sj] = 1
    s.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj] == 0 and\
                    abs(arr[ni][nj]-arr[ci][cj])==1:  # 방문하지 않고, 차가 1이면
                q.append((ni, nj))
                v[ni][nj] = 1
                s.append(arr[ni][nj])

    return min(s), len(s) # 시작지점, 방문한 길이


# 방의 개수가 최대인방이 여러개면 그 중 적힌수가 가장 작은 것 출력

t = int(input())
for t_c in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[0]*n for _ in range(n)]


    start = n*n
    cnt = 0
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                ts, tc = bfs(i, j) # 시작지점, 방문한 길이
                if cnt<tc or tc == cnt and ts < start:
                    cnt = tc
                    start = ts

    print(f'#{t_c} {start} {cnt}')