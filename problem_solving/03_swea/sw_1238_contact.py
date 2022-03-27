from collections import defaultdict, deque
def bfs(s):
    called = [0] * (max(lst)+1)
    q = deque()
    called[s] = 1
    q.append(s)

    while q:
        tmp = q.popleft()
        for t in dic[tmp]:
            if not called[t]:
                called[t] = called[tmp] + 1
                q.append(t)

    # 전화한 번호중 가장 큰 값을 찾음 (마지막에 연락받은 사람들의 번호가 같을 것이기 때문)
    a = max(called)
    max_call=[]
    # 마지막에 연락받은 사람들의 idx를 알아내서, 가장 큰 값을 return
    for i in range(len(called)):
        if called[i] == a:
            max_call.append(i)
    return max(max_call)


for t in range(1, 11):
    l, s = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = defaultdict(list)
    for i in range(0, l, 2):
        dic[lst[i]] += [lst[i+1]]
    mx = bfs(s)

    # 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람
    print(f'#{t} {mx}')



'''
24 2
1 17 3 22 1 8 1 7 7 1 2 7 2 15 15 4 6 2 11 6 4 10 4 2
'''



# def bfs(s):
#     q = deque()
#     v = [0]*101
#     q.append(s)
#     v[s] = 1
#     sol = s
#
#     while q:
#         c = q.popleft()
#         if v[sol] < v[c] or v[sol] == v[c] and sol<c:
#             sol = c
#         for j in range(1, 101):
#             if adj[c][j] and v[j]== 0:
#                 q.append(j)
#                 v[j] = v[c]+ 1
#
#     return sol
#
#
#
# for t in range(1, 11):
#     l, s = map(int, input().split())
#     lst = list(map(int, input().split()))
#     adj = [[0]*101 for _ in range(101)]
#     for i in range(0, len(lst), 2):
#         adj[lst[i]][lst[i+1]] = 1
#     ans = bfs(s)
#
#     # 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람
#     print(f'#{t} {ans}')
#
