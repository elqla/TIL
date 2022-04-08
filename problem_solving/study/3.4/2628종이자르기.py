x, y = map(int, input().split())  #가로 , 세로
# max 100cm
cut = int(input())  #잘라야하는 점선의 개수

xlst = [0, x]
ylst = [0, y]

for i in range(cut): # 최대를 남기고 자르려면 ex) x = 3, b =1 ;(3-1) = 2
    a, b = map(int, input().split())
    if a == 0:  # 가로로 자르는 점선; 가로로 나눔 ; 세로에서 나눠준다
        ylst.append(b)
    elif a == 1:   # 세로
        xlst.append(b)

xlst.sort()  #점선들의 값 크기별로 정렬
ylst.sort()

xx = []
yy = []
for i in range(1, len(xlst)):
    ax = xlst[i] - xlst[i-1]
    xx.append(ax)
for j in range(1, len(ylst)):
    ay = ylst[j] - ylst[j-1]
    yy.append(ay)

area = max(xx) * max(yy)
print(area)






# for i in range(len(xlst)):
#     if i <= x//2:
#         areax = x - max(xlst)
#     else: #i>x//2
#         areax = max(xlst)
#
# for i in range(len(ylst)):
#     if i <= y//2:
#         areay = y - max(ylst)
#     else: #i>y//2
#         areay = max(ylst)













