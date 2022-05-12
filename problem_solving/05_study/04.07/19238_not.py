from collections import defaultdict, deque
n, m, oil = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(int, input().split()) # 운전시작좌표
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

start = []
end = []
for i in range(1, m+1):
    a, b, c, d = map(int, input().split())
    # 승객의 출발지의 행과 열번호, 목적지의 행과 열 번호
    start.append((a-1, b-1))
    end.append((c-1, d-1))
    arr[a-1][b-1] = 's'+str(i)
    arr[c-1][d-1] = 'e'+str(i)
print(arr)

visited = arr[:]  #[x[:] for x in arr]
visited[sx][sy] = 0
start = deque()
start.append((sx, sy))
while start:
    xx, yy = start.popleft()
    bfs()
    for dx, dy in delta:
        nx, ny = xx+dx, yy+dy
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]!=1 and (nx, ny)!=(sx, sy):
            if arr[nx][ny]==0:
                visited[nx][ny] = visited[xx][yy] + 1
            elif arr[nx][ny][0]=='s':
                visited[nx][ny] = visited[xx][yy] + 1
                start.append((nx, ny))
    if len(start)>2:
        # 두개가 있는것




def bfs(sx, sy, oil):
    if oil==0 or str not in arr:
        return


# 최단거리 승객 구하기

# 만약 >1 1명 이상일시, x비교 후 y 비교 ( 작은거 )


# 거리계산
# oilbank==위치 . 최단거리 0
# 목적지로 이동하면서 소모된 연료의 2배 충전 !
# 연료 바닥시, 이동 실패지만 목적지일땐 상관 없음











'''
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
'''



