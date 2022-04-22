from itertools import combinations
from collections import deque
import copy
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 0 빈칸# 1 벽# 2 바이러스 놓을 수 있는 칸
# M개의 바이러스가 상하좌우 빈칸으로 동시복제 - 1초
# 모든칸에 6초면 바이러스 퍼트리기 가능  # 최소시간 구하기

pre_virus = []
visit = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            pre_virus.append((i, j))
        elif arr[i][j]==1:
            visit[i][j] = -1
comb_virus = combinations(pre_virus, M)
# for 문으로 꺼내면 ((0, 0), (1, 5), (4, 3))



min_time = N*N
for virus in comb_virus:
    visited = copy.deepcopy(visit)
    for x, y in virus:
        visited[x][y] = 1  # 출발지점 시간은 0임 , 표시하느라 +1//나중에 -1 빼주기

    q = deque(virus)
    while q:
        i, j = q.popleft()
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0 :
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    zero_count = 0 # 비어있는 공간 cnt
    for v in visited:
        zero_count += v.count(0)
    if zero_count==0:  # 비어있는 공간이 없다면
        time = max(map(max, visited))
        if time < min_time:
            min_time = time
    else:
        continue



if min_time != N*N:      # 비어있어서 min_time이 변경되지 않은경우==바이러스가다 못퍼진 경우
    print(min_time-1)
else:
    print(-1)