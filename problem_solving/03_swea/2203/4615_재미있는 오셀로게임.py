'''

스택, 좌표 넣어주기
보드는 44, 66, 88 가운데 4개에 WB/BW
흑 백 순서

---조건---
상대편의 돌 옆에 놓을 수 있다.
내 돌이 흑이라면
흑 백 흑  이런식으로, 상대편의 돌을 사이에 두어야만 한다.

흑 흑 흑

돌 놓을 곳 없으면 pass

보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면
게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.

'''




t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    # 보드의 길이,  플레이어가 돌을 놓는 횟수



    board = [[0]*n for _ in range(n)]
    # 기존에 있을 돌 색상 표시해주기
    a = n // 2
    board[a - 1][a - 1] = 2
    board[a - 1][a] = 1
    board[a][a - 1] = 1
    board[a][a] = 2

    # 다음에 넣어야할 돌의 위치가 주어지므로
    # 판단해야 할 것
    # 1. 상하좌우대각의 돌 중 '다른색'이 있는지 + '다른색돌'과 인접하여(같은 방향으로) 내 돌이 있는지 확인한다 = > 그래야 놓을 수 있음

    for idx in range(m):
        x, y, dol = map(int, input().split())
        x = x-1
        y = y-1
        # 돌을 놓을 곳을 인풋받고, 보드에서 내 돌 주위 돌들을 확인해본다.
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1,-1]]:
            stack = [] ## 바꿔줄 돌 넣어주기
            for i in range(1, n):
                nx, ny = x+dx*i, y+dy*i
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny] == 0:
                        break
                        # 간 곳이 비어있으면 방향 바꾸기 위해 break
                    elif board[nx][ny] != dol:
                        stack.append([nx, ny])
                        continue
                    else: # 나랑 같은 색이 있어   # 사이의 값들을 같은 색으로 바꿔주기
                        while stack:
                            board[x][y] = dol
                            c, d = stack.pop()
                            board[c][d] = dol
                        break



    #1 흑돌, 2백돌
    b = 0
    w = 0
    for c in board:
        b += c.count(1)
        w += c.count(2)


    print(f'#{tc} {b} {w}')





'''
1
4 12 
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2

'''
