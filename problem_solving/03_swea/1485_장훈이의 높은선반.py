
# 탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고,
# 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.

# 높이가 b 이상인 탑 중, 가장 낮은 탑 ??
def dfs(n, s):
    global ans
    if n==N:
        if s>=b and ans>s-b:
            ans = s-b
        return
    dfs(n+1, s+h_lst[n])
    dfs(n+1, s)


t = int(input())
for tc in range(1, t+1):
    N,b = map(int, input().split())
    # n명의 점원
    # 선반의 높이 b <= 점원의 키의 합
    h_lst = list(map(int, input().split())) # 점원들 키

    ans = 12345678 # 최소 높이
    dfs(0, 0) #0idx, s,

    print(f'#{tc} {ans}')




'''
3
5 16
3 1 3 5 6
2 10
7 7
3 120
83 64 36
'''