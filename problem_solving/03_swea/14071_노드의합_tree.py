t = int(input())
for tc in range(1, t+1):
    # 완전이진트리
    lst = list(map(int, input().split()))
    n = lst[0] # 노드개수
    m = lst[1] # 리프노드개수
    l = lst[2] # 출력할 노드번호

    node=[0]*(n+2) # 노드리스트, 인덱스 맞춰주기
    for _ in range(m):      # 리포노드 입력받기
        a, b = map(int, input().split())
        node[a] = b
    # 리프가 6|5, 4가 주어지는 트리에선 6-3이 연결되어있음
    # 따라서 i*2+1을하면 7이되므로 인덱스가 맞지 않음 (0~n+1까지 node 필요)

    for i in range(n-m, 0, -1):
        node[i] = node[i*2] + node[i*2+1]


    res = node[l]
    print(f'#{tc} {res}')


'''
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962

'''