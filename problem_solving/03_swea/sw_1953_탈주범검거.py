from collections import deque

t = int(input())
for tc in range(1, t+1):

    # 세로 가로 맨홀세로 가로   소요시간
    #  n   m   x        y     l
    n, m, sx, sy, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # l 시간이 지났을때, 탈주범이 위치할 수 있는 장소의 개수를 계산

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 상하좌우(0, 1, 2, 3)
    dic = {
        1: delta,
        2: [delta[0], delta[1]],
        3: [delta[2], delta[3]],
        4: [delta[0], delta[3]],
        5: [delta[1], delta[3]],
        6: [delta[1], delta[2]],
        7: [delta[0], delta[2]]
    }

    opposite = [1, 0, 3, 2]

    q = deque()
    visited = [[0]*m for _ in range(n)] # l시간이 지났을때 탈주범이 위치할 수 있는 곳
    q.append((sx, sy)) #맨홀 위치 넣어줌
    visited[sx][sy] = 1

    #처음 들어갈때, 한시간 소요
    l-=1
    while l>0:
        tmpq = []
        while q:
            x, y = q.popleft()
            k = arr[x][y] #key 임시저장
            for dx, dy in dic.get(k):
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and arr[nx][ny]!=0 and not visited[nx][ny]: # 터널이 있을때
                    # 그 터널이 갈수 있는곳이려면 양방향이여야 함
                    tmp = delta.index((dx, dy)) # 만일 (1, 0) 이면 idx 0
                    dt = opposite[tmp] # 델타는 반대 즉, 1을 가짐
                    if delta[dt] in dic.get(arr[nx][ny]):
                        visited[nx][ny] = 1
                        tmpq.append((nx, ny))

        if tmpq:
            q.extend((tmpq))
            tmpq = []
        l-=1
        # 이동했으니까, 총 2시간 소요


    cnt = 0
    for v in visited:
        cnt += v.count(1)
    print(f'#{tc} {cnt}')

    pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0],
            [1, 0, 1, 0]]
    di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)
    opp = [1, 0, 3, 2]


    # def BFS(N, M, si, sj, L):
    #     q = []
    #     v = [[0] * M for _ in range(N)]
    #
    #     q.append((si, sj))
    #     v[si][sj] = 1
    #     cnt = 1
    #
    #     while q:
    #         ci, cj = q.pop(0)
    #
    #         if v[ci][cj] == L:
    #             return cnt
    #
    #         for k in range(4):
    #             ni, nj = ci + di[k], cj + dj[k]
    #             if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and \
    #                     pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:
    #                 q.append((ni, nj))
    #                 v[ni][nj] = v[ci][cj] + 1
    #                 cnt += 1
    #     return cnt
    #
    #
    # # T = 10
    # T = int(input())
    # for test_case in range(1, T + 1):
    #     N, M, R, C, L = map(int, input().split())
    #     arr = [list(map(int, input().split())) for _ in range(N)]
    #     ans = BFS(N, M, R, C, L)
    #     print(f'#{test_case} {ans}')


'''
1
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0

'''
# 5