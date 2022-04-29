import heapq
# 인접지역 이동시 연료+=1
# 높은곳으로 이동시 연료= 1+ 연료차이


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    def dijkstra(si, sj): # 시작지점
        heap = []
        distance = [[float('inf')]*n for _ in range(n)]
        heapq.heappush(heap, (0, si, sj)) # 좌표
        distance[si][sj] = 0

        while heap:
            pre_cost, i, j = heapq.heappop(heap)
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni, nj = i+di, j+dj
                cost = 1
                if 0<=ni<n and 0<=nj<n:
                    if arr[ni][nj] > arr[i][j]: # 연료가 더 클때
                        cost += arr[ni][nj]-arr[i][j]
                    if distance[ni][nj] > distance[i][j] + cost:  # 새로 이동할 위치에 이미 값이 있는데, 그 값이 현재 값보다 크면 바꿔줌
                        distance[ni][nj] = distance[i][j] + cost
                    else:
                        continue # 이미 있는 값이 더 작거나 같을때 다음 for문 돌도록
                    heapq.heappush(heap, (distance[ni][nj], ni, nj)) ## cost
        return distance[-1][-1]

    print(f'#{tc} {dijkstra(0, 0)}')



'''
1
5
0 1 1 1 0 
1 1 0 1 0 
0 1 0 1 0 
1 0 0 1 1 
1 1 1 1 1
'''
