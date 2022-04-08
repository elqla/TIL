from collections import deque
n, m = map(int, input().split())
# n = 행의 개수.. 세로..

# 각 변/모서리를 기준으로 1 있는지 확인, 찾으면 stop해서 좌표 구하기
# set으로 겹치는 좌표 제거
# 상하좌우로만 찾아보기

arr = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    air = set()
    visited = [[False]*m for _ in range(n)]
    # 모서리 좌표 넣기
    # 좌표가 겹쳐서 들어가지만, set이라서 상관 x
    for i in range(n):
        for j in range(m):
                if i == 0 or i == n-1:
                    air.add((i, j))
                    visited[i][j] = True
                if j == 0 or j == m-1:
                    air.add((i, j))
                    visited[i][j] = True

    # air의 좌표가 남아있을때까지 while문 돌기
    cnt = 0
    while air:
        x, y = air.pop()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                    if arr[nx][ny] == 0 :
                        visited[nx][ny] = True
                        air.add((nx, ny))
                    elif arr[nx][ny]==1:
                        arr[nx][ny] = 0
                        cnt += 1
                        visited[nx][ny] = True

    return cnt


res = []
time = 0
while 1:
    # cnt = 치즈가 녹은 개수
    cnt = bfs()
    res.append(cnt)
    if cnt == 0:
        break
    time += 1
print(time)
print(res)

print(res[-2])





'''
3 3
0 0 0
0 0 0
0 0 0

13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''
