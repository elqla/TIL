import sys

sys.stdin = open('input_1.txt', 'r')


T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) # 마을의 개수
    lst = [list(map(int, input().split())) for _ in range(n)]

    # 충전소 최소 1개, 최대 2개
    # 하나만 놔도 되면 하나만 놓기.
    # 2개 지으면, 가장 가까운 충전소로 사용하기
    # 둘다 충전소를 놔도 못쓰면 -1
    # 집있으면 충전소 못 놓음

    # 충전소를 먼저 놓은 후, 거리의 합이 최소가 되는 값 도출
    # |집x - 충전소x|  + |집y - 충전소y| = 집과 충전소의 거리

    lst = []
    for i in range(-15, 16):
        # for j in range(15, -16, -1):
        lst.append(list([i, x] for x in range(15, -16, -1)))
    print(lst)

    clst = [[0]*31 for _ in range(31)]
    print(clst)

    for i in range(n):
        x = lst[i][0]
        y = lst[i][1]
        c = lst[i][2]
        clst[x][y] = str(i + 1)


        delta = [(0,1), (-1, 0), (0, -1), (1, 0)]
        if c == 1:
            for di, dj in delta:
                lst[x+di][y+dj] += 1
        else:
            q = [(x, y)]
            visited = [[0]*31 for _ in range(31)]
            visited[x][y] = 1
            while q:
                x, y = q.pop(0)
                for xi, yi in range(c)




        dis = lst[i][2]








    print("#%d" % test_case, lst)