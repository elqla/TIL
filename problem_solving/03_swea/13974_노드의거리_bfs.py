from collections import deque, defaultdict


def bfs(v, S, G):
    visited = [0] * (v + 1)  # idx
    q = deque()
    visited[S] = 1
    q.append(S)
    while q:
        t = q.popleft()
        for v in dic.get(t):
            if not visited[v]:
                visited[v] = visited[t] + 1
                q.append(v)
            if v==G:
                return visited[v]-1

    return 0


for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    #노드개수, 간선정보
    dic = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        dic[a] += [b]
        dic[b] += [a]
    '''   
    grid = [[] for _ in range(v+1)]  #idx를 맞춰서, dictionary를 안써도 됨
    for _ in range(e):
        s, g = map(int, input().split())
        grid[s].append(g)
        grid[g].append(s)
    S, G = map(int, input().split())

    a = dfs(S, G, v)
    print(f'#{tc} {a}')
    '''

    S, G = map(int,input().split())
    res = bfs(v, S, G)


    print(f'#{tc} {res}')



'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6 
7 4
1 6
2 3
2 6
3 5
1 5 
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

'''