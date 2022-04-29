# 특정한 두 개의 노드에 경로가 존재하는지 확인
# 경로가 있으면 1, 없으면 0을 출력한다.

from collections import defaultdict
t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    #v개의 노드 1부터 시작, (5~50)
    #e개의 간선(4~1000)


    lst = []
    for _ in range(e):
        s, g = map(int, input().split())
        lst += s, g

    S, G = map(int, input().split())

    graph = defaultdict(list)
    for i in range(0, len(lst), 2):
        a = lst[i]  # 출발노드 1, 2, 4
        b = lst[i+1]
        graph[a] += [b]
        #graph[b] += [a]
    # 양쪽 다 추가하지 X


    stack = [S]  #S에서 시작해서,
    visited = [S] #방문한 곳 저장
    while stack:
        tmp = stack[-1]
        for node in graph[tmp]:  #노드와 연결된 노드들중
            if node not in visited: #아직 방문하지 않은 노드
                stack += [node]
                visited += [node]
                break #stack[-1] 마지막에 방문한 노드를 기준으로 시작
        else:
            stack.pop() #노드와 연결된 곳에 다 방문했으면, stack에서 pop하여 이전으로 돌아감
                        #S라는 출발노드에서, G에 도착했는지, visited를 통해 확인한다.
    if G in visited:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


    '''
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6

{1: [4, 3],
 2: [3, 5],
 3: [1, 2],
 4: [1, 6],
 5: [2],
 6: [4]}

(1,4, 6, 3)
(1, 4, 6, 3, 2, 5)


'''