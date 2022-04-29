from collections import defaultdict, deque

n, m, v = map(int, input().split())
dic = defaultdict(list)
#dic = defaultdict(set)


for _ in range(m):
    a, b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
    # dic[a].add(b)
    # dic[b].add(a)


for i in dic.keys():
    dic[i] = sorted(dic[i])


# dfs
stack = [v]
visited = [v]
while stack:
    tmp = stack.pop()
    for x in dic[tmp]:
        if x not in visited:
            visited.append(x)
            stack.append(x)
            break # 다음 후보로 넘어가지 않기 위함 ! 계속 이어서 방문해줘야 하므로

print(*visited)

# bfs
dq = deque([v])
visit = [v]
while dq:
    tmp = dq.popleft()
    for x in dic[tmp]:
        if x not in visit:
            visit.append(x)
            dq.append(x)
print(*visit)