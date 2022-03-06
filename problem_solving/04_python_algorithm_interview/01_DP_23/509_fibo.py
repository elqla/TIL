from collections import defaultdict
class Solution:
    dp = defaultdict(int)
    def fib(self, n: int) -> int:
        self.dp[1] = 1
        if n>1:
            self.dp[n] = self.dp[n-1] + self.dp[n-2]
        return self.dp[n]

# 메모이제이션
class Solution:
    dp = defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]

# f1 = Solution()
# ans = f1.fib(10)
# print(list(ans))


#타뷸레이션(상향식)
class Solution:
    dp = defaultdict(int)
    def fib(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] =1
        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1]+self.dp[i-2]

        return self.dp[n]


#두 변수
class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y= y, x+y
        return x


#행렬
##.....

#모든 경우의 수를 계산할때, dp를 쓴다
