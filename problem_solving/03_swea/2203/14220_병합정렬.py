def merge_sort(lst):

    if len(lst)==1:
        return lst
    # 가운데 찾고 나눠주기
    mid_i = len(lst)//2
    left = lst[:mid_i]
    right = lst[mid_i:]
    # 반복
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    result = []
    i = j = 0
    left_l = len(left)
    right_l = len(right)
    # 둘 중 하나라도 남아있는데
    while i<left_l or j<right_l:
        # 둘 다 있어야 병합을 할 수 있음
        if left_l>i and right_l>j:
            if left[i]<right[j]: # 왼쪽이 더 작으면
                result.append(left[i])
                i += 1
            else: #우측이 더 작으면
                result.append(right[j])
                j += 1
        else: # 하나만 남았을때
            if i<left_l:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    return result



t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    res = merge_sort(lst)[n//2]# N//2번째 원소

    print(f'#{tc} {res} {cnt}')

'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''