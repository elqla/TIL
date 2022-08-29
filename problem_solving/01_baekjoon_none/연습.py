# n, m = map(int, input().split())
# lst = [list(map(int, input())) for _ in range(n)]

# def mxsum(x, y):
#     tmp = 1
#     for i in range(x, x+n):
#         for j in range(y, y+m):
#             tmp+=lst[i][j]
#     mx.append(tmp)

# mx = []
# nl = len(lst)
# ml = len(lst[0])
# if nl>=n and ml>=m:
#     for i in range(0, len(lst)-n+1):
#         for j in range(0, ml-m+1):
#             mxsum(i, j)

# new_list = list(map(list, zip(*lst)))
# nl = len(new_list)
# ml = len(new_list[0])
# if nl>=n and ml>=m:
#     for i in range(0, len(new_list)-n+1):
#         for j in range(0, ml-m+1):
#             mxsum(i, j)

# print(mx)

######################################################
import sys
input = sys.stdin.readline

# 회의실을 효율적으로 사용하는 방법
# 끝나는 것과 동시에 다음 회의가 시작
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

# 빨리 끝나는 회의 순으로 정렬해서 최대한의 회의수를 고려한다.
lst = sorted(lst, key=lambda x: x[1])



mx = 0
for i in range(1, len(lst)):
    cnt = 1
    start = i-1
    end = i
    breakpoint = 1
    while breakpoint<len(lst) and end<len(lst):
        if lst[start][1]<=lst[end][0]:
            cnt += 1
            start = end
            end = end + 1
        else:
            end = end + 1
        breakpoint += 1
    if cnt > mx:
        mx = cnt
        
print(mx)

'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 12
8 11
2 13
12 14
'''
######################################################
