from collections import defaultdict

# f(1) = 1
# f(2) = 2
# f(3) = 3
# f(4) = 5
# 저장해야할 값: 마지막 f(n)의 값
def climbStairs(n):
    dp = defaultdict(int)  #{key:0}
    dp[1] = 1
    dp[2] = 2
    # if n<=2:
    #     return n
    if dp[n]:
        return dp[n]
    dp[n] = climbStairs(n-1)+climbStairs(n-2)
    return dp[n]

a = climbStairs(10)
print(a)


