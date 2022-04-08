# O로 표시된 칸의 말 잡을 수 있음
# 색칠된부분 놓일수 없음
# 서로가 서로를 잡을 수 없도록 놓는다면 최대 몇개의 비숏을 놓을 수 있을까
# 색칠된 부분에는 비숍이 놓일 수 없지만 지나갈 수는 있다.
# 대각

# 비숍을 놓을 수 있는 곳은 1이지만
# 비숍이 갈때 비숍이 있으면 안되니까 비숍이 있던 자리는 '#' 표시를 해주기
def chess(arr):
    def dfs(i, j):
        # 비숍이 가는곳에 비숍이 있으면 가지말고, 종료
        if i<0 or i>=n or j<0 or j>=n or arr[i][j] == '#':
            return


        elif arr[i][j] == 1:
            arr[i][j] = '#'


        # 대각선으로 탐색
        dfs(i+1, j+1)
        dfs(i-1, j+1)
        dfs(i-1, j-1)
        dfs(i+1, j-1)

    mx = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] ==1:
                arr[i][j] = '#'
                dfs(i, j)

        cnt = 0
        for a in arr:
            cnt += arr.count('#')
        if cnt > mx:
            mx = cnt
    return mx


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = chess(arr)
print(res)




'''
5
1 1 0 1 1
0 1 0 0 0
1 0 1 0 1
1 0 0 0 0
1 0 1 1 1


출력 
7
'''





