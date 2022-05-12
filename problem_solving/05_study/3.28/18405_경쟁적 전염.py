# s초가 지난 후 x, y에 있는것 ?

# 1초마다, 상하좌우의 방향으로 증식해나감
# 단, 번호가 낮은 종류의 바이러스부터 증식함
# 이미 있으면 못함 #visited

# s초 이후, x,y에 존재하는 바이러스의 종류는 ?
# visited = [[0]*n for _ in range(n)]

from collections import deque
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
x = x-1
y = y-1

dq = []
for i in range(n):
    for j in range(n):
        if arr[i][j] !=0:
            dq.append((arr[i][j],i, j, 0))
dq.sort()
dq = deque(dq)
while dq:
    sort, i, j, time = dq.popleft()
    if time == s:
        break
    else:
        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==0:
                arr[ni][nj] = sort
                dq.append((sort, ni, nj, time+1))

print(arr[x][y])


'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2
'''
