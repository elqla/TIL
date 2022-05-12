N = int(input())  #1~1000이하로 주어짐
# l, h = map(int, input().split())  #l = idx  1~1000이하로 주어짐


arr = [list(map(int, input().split())) for _ in range(N)]
# l,h
arr.sort() #[[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

mx = 0
for i in range(len(arr)):
    if arr[i][1] > mx:
        mx = arr[i][1]
        top = i
cnt = arr[top][1]

cnt1 = 0
mxi = arr[0][0] #밑 인덱스
mx = arr[0][1] #높이
for i in range(1, top+1):
    if mx < arr[i][1]:
        cnt1 += (arr[i][0]-mxi)*mx  #밑변 * 높이
        mxi = arr[i][0] #밑인덱스
        mx = arr[i][1] #높이

cnt2 = 0
mxi = arr[-1][0] #밑 인덱스
mx = arr[-1][1] #높이
for i in range(len(arr)-1, top-1, -1):
    if mx < arr[i][1]:
        cnt2 += (mxi-arr[i][0]) * mx  # 밑변 * 높이
        mxi = arr[i][0]  # 밑인덱스
        mx = arr[i][1]  # 높이

print(cnt + cnt1 + cnt2)

