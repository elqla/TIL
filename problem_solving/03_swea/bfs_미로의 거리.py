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
# sti, stj = -1, -1
# for i in range(n):
#     for j in range(n):
#         if maze[i][j]==2:
#             sti, stj =i, j
#             break #j for문 하나만 빠져나감
#     if str != -1:
#         break


def fstart(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j
    return -1,-1 #없어도됨

def bfs(i, j, n):
    visited = [[0]*n for _ in range(n)] #미로의 크기만큼 생성
    queue = [] #큐 생성
    queue.append((i, j)) #시작점 v를 큐에 삽입
    visited[i][j] = 1 #시작점 방문표시
    while queue: #큐가 비어있지않으면 반복
        # 모든 작업은 pop 한 다음에 합시다.
        i, j = queue.pop(0)# t<-디큐 #앞에서 뽑기
        if maze[i][j] == 3: # visit(t) t에서 할일처리
            return visited[i][j] -2  #중간에 거쳐가는 칸 수 출력(-2 = 출발, 도착 칸 제외)
        for di, dj in [[0, 1], [1, 0],[0, -1],[-1, 0]]:  # i, j 에 인접한 칸에 대해
            ni, nj = i+di, j+dj     #주변 칸 좌표
            if 0<=ni<n and 0<=nj<n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                #벽이 아닌곳=통로와 도착지가 포함됨, 통로인곳 하면 도착지 3인 곳도 제외시켜버림
                queue.append((ni, nj))#인접하고 방문하지 않은곳을 찾았어 ! 인큐
                visited[ni][nj] = visited[i][j] + 1
    # 도착지를 찾지 못한경우
    return 0 #while을 다 돌고 빠져나올때의 동작




t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    sti, stj = fstart(n)
    ans = bfs(sti, stj, n)
    print(f'#{tc} {ans}')

















