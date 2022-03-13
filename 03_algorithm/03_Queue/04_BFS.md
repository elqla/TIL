```python
# 인풋받기
input_str = "1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7"
lst = list(map(int,input_str.split(", ")))

# 그래프 만들기
from collections import defaultdict
graph = defaultdict(list)

for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]    
    graph[a].append(b)
    graph[b].append(a)


# 큐 생성
queue = []
visited = []

queue.append(1)
visited.append(1)

# BFS
while queue:
    # deQueue
    tmp = queue.pop(0)

    for node in graph[tmp]:
        if node not in visited:
            queue.append(node)
            visited.append(node)
    print(queue)
    # [2, 3]
    # [3, 4, 5]
    # [4, 5, 7]
    # [5, 7, 6]
    # [7, 6]
    # [6]
    # []


# BFS, visited가 tmp 아래 있으면 비효율 발생

queue = []
visited = []

queue.append(1)

# BFS
while queue:
    # deQueue
    tmp = queue.pop(0)
    visited.append(tmp)

    for node in graph[tmp]:
        if node not in visited:
            queue.append(node)
    print(queue)
    
# [2, 3]
# [3, 4, 5]
# [4, 5, 7]
# [5, 7, 6]
# [7, 6, 6]
# [6, 6, 6]
# [6, 6]
# [6]
# []

```