n = int(input()) #색종이 수


arr = [[0]*100 for _ in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            if arr[x+j][y+k] == 0:
                arr[x+j][y+k] = 1


cnt = 0
for a in arr:
    cnt += a.count(1)

print(cnt)

# ###
# N = int(input())
# white = [[0] * 100 for _ in range(100)]
# for i in range(N):
#     x, y = map(int, input().split())
#     for row in range(x, x+10):
#         white[row][y:y+10] = [1] * 10
#
#
#
# area = 0
# for w in white:
#     area += sum(w)
# print(area)



