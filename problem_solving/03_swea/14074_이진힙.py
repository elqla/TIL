t = int(input())
for tc in range(1, t + 1):
    n = int(input())  # 주어질 n개의 자연수
    tree = list(map(int, input().split()))

    import heapq

    heap = []
    for i in tree:
        heapq.heappush(heap, i)



    #heapq.heapify(tree)  # 최소힙

    heap = [0] + heap  # idx 맞춰주기

    par = [0] * (n + 1)  # 자식 idx에 부모값 넣어주기
    for i in range(1, n + 1):
        par[i] = heap[i // 2]

    s = 0  # 조상노드를 더해줄 변수
    while n != 0:  # 마지막 노드의 부모노드가 0이 아닐때까지  ## n은 노드의 인덱스 !
        s += par[n]
        n = n // 2  # 부모 인덱스 넘겨주기
    print(f'#{tc} {s}')


'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40

'''