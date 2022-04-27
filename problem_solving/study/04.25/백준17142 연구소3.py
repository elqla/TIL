# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

# NXN 칸의 연구소
# 바이러스 M개를 활성상태로 변경


# 조합으로 활성바이러스 고르기
# 비활성바이러스 활성화시켜서 퍼뜨리기

from collections import deque
from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


virus = []
blank = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:  #  virus 구하기
            virus.append((i, j))
        elif arr[i][j] ==0:
            blank += 1   # 통로 개수 세기


mn = N*N
viruses = combinations(virus, M)
for comb in viruses:
    dq = deque(comb)
    visited = [[-1]*N for _ in range(N)]
    for i, j in comb:
        visited[i][j] = 0
    remain = blank # 통로 개수
    while dq:
        if remain == 0:
            break
        i, j = dq.popleft()
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0<=nj<N and 0<=ni<N and visited[ni][nj]==-1:  # 비어있는곳만 가기
                if arr[ni][nj] != 1:
                    dq.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
                    if (ni, nj) not in virus:
                        remain -=1

    if remain:
        continue
    else:
        time = 0
        for v in visited:
            time = max(time, *v)
        if time < mn:
            mn = time
if mn==N*N:
    mn = -1
print(mn)
