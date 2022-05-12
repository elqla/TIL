delta = [[0, 0, -1, 1],
         [1, -1, 0, 0]]


R, C = map(int, input().split())
# R행 C열
map = [list(input()) for _ in range(R)]
# 비어있는 곳은 '.'로 표시되어 있고,
# 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다.
# 비버의 굴은 'D'로, 고슴도치의 위치는 'S'

# 고슴도치, 물 -비어있는칸 이동, 돌로이동 X  비버의 소굴로 이동 X
# 고슴도치->비버의 소굴로 이동하기 위한 최소시간
from collections import deque
gos = deque()
water = deque()
for r in range(R):
    for c in range(C):
        if map[r][c]=='S':
            gos.append((r,c))
        elif map[r][c]=='*':
            water.append((r,c))

mn = 0
flag = 0
while gos:
    l = len(water)
    while l:
        wi, wj = water.popleft()
        for i in range(4):
            ni, nj = wi + delta[0][i], wj + delta[1][i]
            if 0<=ni<R and 0<=nj<C and (map[ni][nj]!='X' or map[ni][nj]!='D'):
                if map[ni][nj]=='S':
                    if gos:
                        map[ni][nj] = '*'
                        if (ni,nj) in gos:
                            gos.remove((ni, nj))
                    else:
                        print('KAKTUS')
                        flag = 1      #더 갈수있는 고슴도치가 없을때
                        break
                elif map[ni][nj]=='.':
                    map[ni][nj] = '*'
                    water.append((ni, nj))
        if flag:
            break
        l-=1
    gl = len(gos)
    while gl:
        gi, gj = gos.popleft()
        for i in range(4):
            ni, nj = gi + delta[0][i], gj + delta[1][i]
            if 0<=ni<R and 0<=nj<C and (map[ni][nj]!='X' or map[ni][nj]!='*'):
                if map[ni][nj]=='D':
                    mn += 1
                    print(mn)
                    flag = 1
                elif map[ni][nj]=='.':
                    map[ni][nj] = 'S'
                    gos.append((ni, nj))

        if flag:
            break
        gl -=1
    mn += 1
    if flag:
        break
else:
    print('KAKTUS')



'''

3 3
D.*
...
.S.
        
'''


