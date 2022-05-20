def recur(m, total, arr2):  # 구간에서 최대 액수 구하기
    global mx_h
    if total>C:   # C보다 크면 return
        return
    if m == M:  # 구간을 다 확인했으면 최댓값 갱신
        mx_h = max(mx_h, arr2)
        return
    recur(m+1, total, arr2)  #선택 or not
    recur(m+1, total+tmp[m], arr2 + tmp[m]**2)



t = int(input())
for tc in range(1, t+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr2 = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            mx_h = 0
            tmp = arr[i][j:j+M] # 0, 1   # 구간을 배열에 담아, 재귀함수로 최대액수를 찾아줌
            recur(0, 0, 0)
            arr2[i][j] = mx_h

    mx_h = []
    mx_result = 0
    for i in range(N):
        mx_h.append((max(arr2[i]), i)) # 각 라인별로 최댓값을 뽑음
    mx_h.sort(reverse=True)
    mx_result = mx_h[0][0] + mx_h[1][0]



    for i in range(1, N):
        idx = mx_h[i][1]
        # 정렬한 배열 중 최댓값과 동일한 것이 여러 개 있으면 다 골라준다.
        for j in range(N):  # 0  M= 2  0,1
            for k in range(j+M, N): #2    2
                mx_result = max(mx_result, arr2[idx][j] + arr2[idx][k])

    print(f'#{tc} {mx_result}')

'''
10
4 2 13
6 1 9 7
9 8 5 8
3 4 5 3
8 2 6 7
3 3 10
7 2 9
6 6 6
5 5 7
4 1 10
8 1 8 2
4 6 1 6
4 9 6 3
7 4 1 3
'''