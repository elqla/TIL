import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
# h번
# mmmmmm  n
# mmmmmm  n


# 3차원 배열
arr = [[list(map(int, input().split())) for _ in range(n)]for _ in range(h)]

# 1, 익은 / 0, 안익은/ -1, 없는



# arr 을 visited처럼 사용해서 다음날이 되면, 안익은 거를 익은거로 표시!
q = deque() # 익은 토마토 좌표 넣기
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j]==1:
                q.append([k, i, j])


dk = [0, 0, 0, 0, -1, 1] #위아래 상자
di = [1, -1, 0, 0, 0, 0] #상하좌우
dj = [0, 0, -1, 1, 0, 0]

while q:
    k, i, j = q.popleft()
    for d in range(6):  #만약 i, j, k의 옆에 안익은 토마토가 있다면
        nk, ni, nj = k+dk[d], i+di[d], j+dj[d]
        # 안익은것을 익혀서 큐에 넣어주고, arr에 표시
        if 0<=nk<h and 0<=ni<n and 0<=nj<m: # 안익었을때만 고려해주면 됨
            if arr[nk][ni][nj] == 0:
                arr[nk][ni][nj] = arr[k][i][j] + 1 # 익혀서
                q.append([nk, ni, nj]) #큐에 넣어줍니다
            # else: # 익은거나, 토마토가 없거나, 좌표가 상자안에 없으면 다음 위치 찾기
            #     continue


flag = 0
result = -2  # -1이 max일 수도 있어서 (토마토 박스가 비어서)
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 0:
                flag = 1
                # 높이, x,y 순서
            result = max(result, arr[k][i][j])

if flag == 1:  # 안익은상태
    print(-1)
else:              # day를 구하는거니까 원래 토마토(1) 빼줌
    print(result-1) # 토마토가 익어있는 상태이면




'''
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

'''