def dfs(i, j, cnt, k):
    global res
    if res < cnt + 1:
        res = cnt + 1

    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<n and not visited[ni][nj]: # 새로 간 곳이 더 크면 깎아도 갈 수 없으므로 고려하지 않음
            if arr[ni][nj]<arr[i][j]: # 새로 간 곳이 더 작으면
                visited[ni][nj] = 1
                dfs(ni, nj, cnt + 1, k)
                visited[ni][nj] = 0
            elif arr[ni][nj]-k < arr[i][j] and k !=0 : # 같으면 깎기
                tmp = arr[ni][nj]
                arr[ni][nj] = arr[i][j] -1
                visited[ni][nj] = 1
                dfs(ni, nj, cnt + 1, 0)
                arr[ni][nj] = tmp
                visited[ni][nj] = 0



t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    # 한변의 길이, 최대 공사가능 깊이
    arr = [list(map(int, input().split())) for _ in range(n)]

    mx = max(map(max, arr))

    mx_lst = [] # 가장 높은 봉우리들
    for i in range(n):
        for j in range(n):
            if arr[i][j]==mx:
                mx_lst.append((i, j))

    res = 0
    for i, j in mx_lst:
        visited = [[0]*n for _ in range(n)]
        visited[i][j] = 1
        dfs(i, j, 0, k) #i, j, cnt


    # 가장 긴 등산로의 길이
    print(f'#{tc} {res}')

'''
3
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2
1 2 1
2 1 2
1 2 1
5 2
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
'''