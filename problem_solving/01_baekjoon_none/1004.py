import sys
sys.stdin = open('input.txt', 'r')

'''
T = int(input())
sx, sy, ex, ey
n줄에 걸쳐, 
행성계의 중점과 반지름 cx, cy, r

진입횟수 count: 도착지에 포함된 행성
이탈횟수 count: 출발지에 포함된 행성
-> 즉, 둘다 속하거나 속하지 않으면 countX / 둘 중 하나만 속하면 countO
! 출발지와 도착지가 다르나, 한 행성 안일경우 고려 X
'''


T= int(input())
for _ in range(1, T + 1):
    sx, sy, ex, ey = map(int, input().split()) #출발지, 도착지

    planet_cnt = 0
    for _ in range(int(input())):
        cx, cy, r = map(int, input().split())
        d1 = ((sx-cx)**2 + (sy-cy)**2)**0.5
        d2 = ((ex-cx)**2 + (ey-cy)**2)**0.5
        if(d1<r and d2>r) or (d2<r and d1>r):
            planet_cnt += 1
    print(planet_cnt)
    