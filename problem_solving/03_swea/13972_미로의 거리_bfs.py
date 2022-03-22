from collections import deque


def start(maze):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j
    return -1, -1


# 2출발, 3도착
# 0통로, 1벽

t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    maze = [list(map(int, input())) for _ in range(n)]

    sti, stj = start(maze)

    visited = [[0] * n for _ in range(n)]  # 방문한 곳을 지나갈때 추가해줄것
    visited[sti][stj] = 1
    q = deque()
    q.append((sti, stj))  # 출발좌표
    # 최소한의 칸수를 구해야 함

    res = 0
    while q:
        i, j = q.popleft()
        if maze[i][j] == 3:
            res = visited[i][j] - 2
            break
        else:
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1

    print(f'#{tc} {res}')

    # 처음에 visited[ni][nj]==0을 생각하지 못했다, bfs의 특성상 방문하지 않은 곳을 방문해나가는데 아래와 같은 식을 썼다.
'''
    res = 0
    while q:
        i, j = q.popleft()
        maze[i][j] = 1
        if maze[i][j] == 3:
            res = visited[i][j] - 2
            break  #break를 안해주면 무한루프에 빠진다.
        else:
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and maze[ni][nj] !=2:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1

    print(f'#{tc} {res}')



'''

#
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     maze = [list(map(int, input())) for _ in range(n)]
#     #print(maze)
#     sti, stj = fstart(n)
#     ans = bfs(sti, stj, n)
#     print(f'#{tc} {ans}')
#
#
#         for di, dj in [[0, 1], [1, 0],[0, -1],[-1, 0]]:
#             ni, nj = i+di, j+dj     #이렇게 표현도 가능
#
#

'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

'''
