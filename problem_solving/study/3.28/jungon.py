def check(x):
    t = list(map(int, x))

    for i in range(1, len(t)):
        if t[i-1]<=t[i]:
            continue
        else:
            return
    return x

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = input().split()

    res = 0
    a_lst = [] # 단조증가하는 수들을 넣음  # 12 34 56 --74--  23
    for l in lst:
        x = check(l)
        a_lst.append(int(l))


    b_lst = [] #곱해서 넣어줄 리스트
    for i in range(1, len(a_lst)):
        if a_lst[i-1] <= a_lst[i]:  # 단조증가하는 수들을 넣긴했는데, 뭐가 큰진 모름 # 따라서, 대소비교해서 넣어줌
            b = a_lst[i-1]*a_lst[i]
            nb = check(str(b))  # 곱한 수가 단조증가하는지
            if nb: b_lst.append(b)
        else:
            res = -1  # 대소비교중 하나라도 단조증가하지 않으면, -1
                      ## 12 34 56 -- 23--
    print(b_lst)
    mx = max(b_lst)

    if res == -1:
        mx = -1

    print(f'#{tc} {mx}')


'''
1
3
12 34 64

'''

'''
2
4
2 4 7 10
3
1 2 1
'''