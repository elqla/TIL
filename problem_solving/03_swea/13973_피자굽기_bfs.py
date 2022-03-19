from collections import deque

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    # n 화덕의 크기
    # m 피자의 개수
    # 치즈의 양

    C = list(map(int, input().split()))
    oven = deque()
    oven.extend([x for x in range(n)]) # [0, 1, 2]

    cnt = n
    while len(oven) > 1: # 오븐에 하나만 남으면 종료
        t = oven.popleft()
        # 치즈가 없으면서, 피자갯수가 안맞을때 추가
        if cnt < m and not C[t]:
            oven.append(cnt)
            new = C[cnt]
            C[cnt] = new // 2
            cnt += 1
        # 치즈가 있을때는 다시 어팬드
        elif C[t]:
            C[t] = C[t] // 2
            oven.append(t)
    res = list(oven)
    ii = 0
    for i in res:
        ii = i
    print(f'#{tc}', ii+1)

    # #melt = [0]*(m) 처음에 melt라는 리스트를 만들었는데
    # 치즈의 양을 줄이는거고, 고정되어 있으며
    # 순회하는데 있어 필요한것은 oven에 있는 인덱스 값이므로
    # 인풋받은대로 사용해도 됨


'''
3
3 5 
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2
'''







