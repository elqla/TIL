
# 접수창구 N개
# 정비창구 M개

# 접수창구 번호 and 정비창구 번호 이용한 고객
from collections import deque

t = int(input())
for tc in range(1, t+1):

    N, M, K, A, B = map(int, input().split())
    # 2 2 6 1 2

    reception = [0] + list(map(int, input().split()))  # N+1
    print(reception)
    # 0 3 2
    reception_time = [0]*(N+1)


    repair = [0] + list(map(int, input().split()))   # M+1
    # 0 4 2
    repair_time = [0]*(M+1)
    time = list(map(int, input().split())) #list(map(int, input().split()))# k+1 번째 고객
    # 0 0 1 2 3 4
    # 고객번호랑 저장 enumerate


    reception_wait = deque([time[0]])
    repair_wait = deque()

    while reception_wait:
        reception_wait.popleft()
        # receprion time 에서 하나씩 빼서

    #
    #     for i in range(1, N+1):
    #         if reception[i]
    #
    #
    #
    #     if not q:
    #         print(q)
    #     else:
    #         pass
    #
    # while
    #
    #
    # res = -1
    # if reception
    #




    print(f'#{tc}')


'''
10
2 2 6 1 2
3 2
4 2
0 0 1 2 3 4


'''