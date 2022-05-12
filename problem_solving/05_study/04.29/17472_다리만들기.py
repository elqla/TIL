# 한 다리의 방향이 중간에 바뀌면 안된다
# 다리의 길이는 2 이상이어야 한다.
# 다리는 겹칠수 있다.


from collections import deque, defaultdict

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]


# 0 바다 1 땅
# 연결불가능시 -1

def find_island():  # 연결된 섬 찾기
    while q:
        global island_number
        i, j = q.popleft()
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and visited_island[ni][nj]==0:
                q.append((ni, nj))
                visited_island[ni][nj] = 1
                all_island[island_number].append((ni, nj))




mn = 0
island_number = 0
bridge_num = 0
all_island = [[] for _ in range(7)]
dic = defaultdict(list)

visited_island = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        q = deque()
        if arr[i][j] == 1 and visited_island[i][j]==0: # 섬이면서 새로운 섬이면
            island_number += 1  ## island_number 을 키값으로 가짐
            q.append((i, j))
            all_island[island_number].append((i, j))
            visited_island[i][j] = 1
            find_island()

island_num = 1
while island_num!=island_number:
    mn_island = max(N, M)
    arrive_island_num = 0
    for i, j in all_island[island_num]: ## dfs 돌려서 쭉 가보기..  ## 섬 a에서 다른 섬들을 갈때, 다리의 길이가 가장 짧은 섬 가기
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            bridge = 0
            arrive = list()
            for k in range(max(N, M)):       #while True:
                ni, nj = i + di*k, j + dj*k
                if 0 <= ni < N and 0 <= nj < M and ((ni, nj) not in all_island[island_num]):   # 같은 섬이 아닐경우
                    # 방문하지 않았으면서
                    # 새로운 섬이거나, 바다일때를 고려
                    # if bridge>mn_island: # 가지치기
                    #     break
                    if arr[ni][nj]==0: # 바다면
                        bridge += 1
                        continue
                    else: # 새로운 섬이면 도착한거니까
                        if bridge>1 and bridge<mn_island: # 다리가 1보다 길면서 + 최소의 다리길이를 가질때
                            # 이 새로운 섬이 이미 연결된 섬인지 고려
                            for d in range(1, island_number+1): # 1, 2, 3, 4
                                # arrive_island_num = d
                                # mn_island = bridge
                                # arrive = (ni, nj)
                                if (ni, nj) in all_island[d]  and d != island_num:      # 2번섬에서 출발 -   1번섬에서 방문을 했어.
                                    if island_num not in dic[d]:  # 도착한 섬이 이전에 갔던 곳이라면, 키값으로 존재할 것이기 때문  # 2 not in 1:[]
                                        arrive_island_num = d  # 즉, 이전에 방문하지 않은 곳이면 _ !
                                        mn_island = bridge
                                        arrive = (ni, nj)
                                        break
                                # else:
                                #     arrive_island_num = d # 이전에 방문했던 곳이 아니면서, 딕셔너리
                                #     mn_island = bridge
                                #     arrive = (ni, nj)
                            # 길이 ?

    if mn_island != max(N, M):   # 다리를 찾았으면 mn 값에 더해주기
        mn += mn_island
        bridge_num += 1
        dic[island_num].append(arrive_island_num)  # 현재 island_num에 방문한 곳을 넣어주기
    island_num +=1

#span 트리에 저장된 노드
print(dic)
if mn != 0 and island_num-1 == bridge_num:
    print(mn)
else:
    print(-1)
##  이미 서로 연결된 섬들을 계속 최소값으로 인식할 수도 있으므로
##  이미 서로 연결된 경우를 쌍으로 묶어서(sort)

