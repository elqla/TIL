from collections import deque

def dfs(S, G, v):  # start
    visited = [0] * (v + 1)
    q = deque([S])
    visited[S] = 1
    while q:  # visited[G]==0설정해서, 방문하면 while문이 끝났을때로 설정할 수 있음
        t = q.popleft()
        for g in grid[t]:
            if not visited[g]:
                q.append(g)
                visited[g] = visited[t] + 1
            if G==g:
                return visited[G] - 1

    return 0


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    # v개의 노드개수 # 방향성 없는 e개의 간선정보

    grid = [[] for _ in range(v+1)]
    for _ in range(e):
        s, g = map(int, input().split())
        grid[s].append(g)
        grid[g].append(s)
    S, G = map(int, input().split())

    a = dfs(S, G, v)
    print(f'#{tc} {a}')




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