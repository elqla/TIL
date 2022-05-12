import sys
input = sys.stdin.readline
# 어떤 방향으로라도 4군데만 채우면 됨
# 갔던곳 안가고
def dfs(i, j, idx, s):  #
    global mx
    if s + mx_v*(4-idx) <= mx:
        return
    if idx==4:
        if mx < s:
            mx = s
        return
    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<m and not visited[ni][nj]:
            if idx==2:
                visited[ni][nj] = 1
                dfs(i, j, idx+1, s+arr[ni][nj])
                visited[ni][nj] = 0
            visited[ni][nj] = 1
            dfs(ni, nj, idx+1, s+arr[ni][nj])
            visited[ni][nj] = 0



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 정사각형 4개를 이어붙인 것: 테트로미노
mx_v = max(map(max, arr))
mx = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j , 1, arr[i][j])
        visited[i][j] = 0
print(mx)