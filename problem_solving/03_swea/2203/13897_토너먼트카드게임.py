def merge_sort(lst):
    # lst = [(1, 1), (2, 3), (3, 2), (4, 1)]
    # lst 반으로 나누기
    if len(lst)==1:
        return lst
    mid_i = len(lst)//2
    l = merge_sort(lst[:mid_i])
    r = merge_sort(lst[mid_i:])
    # # 한명씩 비교하기 위함


    left = l[0]
    right = r[0]


    if left[1] == right[1]:
        return l
    elif left[1] !=3 and right[1] != 3: # 1, 2(2승리)
        if left[1]>right[1]:
            return l
        else:
            return r
    elif left[1] !=1 and right[1] !=1: # 둘다 1이 아닐때
        if left[1] > right[1]:
            return l
        else:
            return r
    else:  # 1, 3 (1승리)
        if left[1] > right[1]:
            return r
        else:
            return l



t = int(input())
for tc in range(1, t+1):
    N = int(input()) # 인원수

    alst = list(map(int, input().split()))
    lst = []
    for idx, item in enumerate(alst, start=1):
        lst.append((idx, item))

    # lst = list(enumerate(map(int, input().split()), start=1))
    res = merge_sort(lst)


    print(f'#{tc}', res[0][0])






'''

3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
 
'''