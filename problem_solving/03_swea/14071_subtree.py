def pre(n):  # 전위순회
    global cnt
    cnt += 1
    if ch1[n]:
        pre(ch1[n])
    if ch2[n]:
        pre(ch2[n])


t = int(input())
for tc in range(1, t+1):
    e, n = map(int, input().split())
    # 간선의 개수, 루트노드 n

    # 이진트리에서 노드 n을 루트로 하는 서브트리에 속한 노드의 개수를 알아내기
    # 자식노드 인덱스 정리

    v = e+1 # 정점개수 1234
    ch1 = [0]*(v+1)
    ch2 = [0]*(v+1) #idx  01234
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i+1]  #01 23
        if ch1[p] ==0:
            ch1[p] = c
        else:
            ch2[p] = c



    cnt = 0
    pre(n)
    print(f'#{tc} {cnt}')


    '''
3
5 1
2 1 2 5 1 6 5 3 6 4 
5 1
2 6 6 4 6 5 4 1 5 3 
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
    '''