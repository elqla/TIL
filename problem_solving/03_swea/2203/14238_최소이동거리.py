from collections import defaultdict
import heapq

t = int(input())
for tc in range(1, t+1):
    N, E = map(int, input().split()) # 마지막 연결지점 번호, 도로의 개수

    graph = defaultdict(list)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))  # 출발지점 = (도착지점, weight)

    def dijkstra(s):
        q = []
        distance = [float('inf') for _ in range(N+1)]
        heapq.heappush(q, (0, s)) # 최단경로, 시작지점
        distance[s] = 0

        while q:
            cost, s = heapq.heappop(q)

            if distance[s] < cost:  # distance의 값이 cost보다 작을때, 즉 inf>cost 므로,걸림
                continue
            for e, w in graph[s]:
                cost2 = cost + w
                if cost2 < distance[e]: # 처음 계산한 경로보다, 새로 간 경로가 더 짧을때
                    distance[e] = cost2
                    heapq.heappush(q, (cost2, e))

        return distance[N]

    res = dijkstra(0)


    # def dijkstra(s):
    #     U = {s}  # 출발점
    #     distance = [float('inf') for _ in range(N+1)] # 0부터 시작하는 노드들의 거리
    #     distance[s] = 0  # 출발지점 weight 표시
    #
    #     for e, w in graph[s]:
    #         distance[e] = w  # 도착 지점에 weight값을 넘겨줌
    #
    #     for _ in range(N):
    #         min_val = float('inf')
    #
    #         for i in range(N):
    #             if i not in U and min_val>distance[i]:
    #                 min_val = distance[i]
    #                 idx = i
    #         U.add(idx)
    #
    #         for e, w in graph[idx]:
    #             distance[e] = min(distance[e], distance[idx] + w)
    #     return distance[N]
    #
    # res = dijkstra(0)
    print(f'#{tc} {res}')





'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

'''