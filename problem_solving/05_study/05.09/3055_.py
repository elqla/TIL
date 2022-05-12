delta = [[0, 0, -1, 1],
         [1, -1, 0, 0]]

#########고슴도치 먼저 이동하고, 물로 덮음##########
R, C = map(int, input().split())
map = [list(input()) for _ in range(R)]

# 비어있는 곳은 '.'로 표시되어 있고,
# 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다.
# 비버의 굴은 'D'로, 고슴도치의 위치는 'S'

# 고슴도치, 물 -비어있는칸 이동, 돌로이동 X  비버의 소굴로 이동 X
# 고슴도치->비버의 소굴로 이동하기 위한 최소시간
visit = [[0]*C for _ in range(R)]
from collections import deque
gos = deque()
water = deque()
biber = ''
for r in range(R):
    for c in range(C):
        if map[r][c]=='S':
            gos.append((r,c))
            map[r][c] = 0
        elif map[r][c]=='*':
            water.append((r,c))
            visit[r][c] = 1
        elif map[r][c]=='D':
            biber = [r, c]

mn = 0
while gos:
    gi, gj = gos.popleft()
    for i in range(4):
        ni, nj = gi + delta[0][i], gj + delta[1][i]
        if 0<=ni<R and 0<=nj<C and (map[ni][nj]!='X' or map[ni][nj]!='*'):
            if map[ni][nj]=='.':
                map[ni][nj] = map[gi][gj] + 1
                gos.append((ni, nj))
            elif map[ni][nj]=='D':
                mn = map[gi][gj] + 1
                map[ni][nj] = mn
                break
print(map)


while mn:
    tmp = []
    while water:
        wi, wj = water.popleft()
        for i in range(4):
            ni, nj = wi + delta[0][i], wj + delta[1][i]
            if 0<=ni<R and 0<=nj<C and (map[ni][nj]!='X' or map[ni][nj]!='D') and not visit[ni][nj]:
                    # visited가 하나 더 많으므로 하나 빼줌
                    visit[ni][nj] = visit[wi][wj] + 1
                    map[ni][nj] = '*'   # 숫자이거나, 비어있을떄
                    tmp.append((ni, nj))
    mn -=1
    water.extend(tmp)

if map[biber[0]][biber[1]] =='D' or map[biber[0]][biber[1]]=='*':
    print('KAKTUS')
else:
    print(map[biber[0]][biber[1]])
