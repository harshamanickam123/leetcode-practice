class Solution:
    def fib(self, n: int) -> int:
        def rec(n,dp):
            if n<=1:
                return n
            if dp[n]!=-1:
                return dp[n]
            dp[n]=rec(n-1,dp)+rec(n-2,dp)
            return dp[n]
        dp=[-1]*(n+1)
        return rec(n,dp)