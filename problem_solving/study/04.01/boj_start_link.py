import sys
input = sys.stdin.readline

def dfs(idx, start, link):
    # start에 들어갈 사람을 추가 0, 1사람
    # link에 들어갈 사람을 추가 2, 3사람
    global mn
    if len(start) > n//2 or len(link) > n//2:
        return
    #print(start, link)
    if idx == n:  # n=4; idx = 4th 사람수가 결정이 되면
        if len(start)==len(link):  # 반반 나눠졌을때
            asum = bsum = 0
            for i in range(n//2):  # 모든 조합
                for j in range(n//2):
                    asum += arr[start[i]][start[j]]
                    bsum += arr[link[i]][link[j]]
            if mn > abs(asum - bsum):
                mn = abs(asum - bsum)
        return
    dfs(idx+1, start + [idx], link)
    dfs(idx+1, start, link+[idx])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

mn = 1e9
dfs(0, [], [])
# idx, start, link

print(mn)

'''
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
'''

















