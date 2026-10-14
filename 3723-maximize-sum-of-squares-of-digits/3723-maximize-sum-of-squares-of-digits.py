class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num:
            return ""
        a=""
        for i in range(num):
            d=min(9,sum)
            a+=str(d)
            sum-=d
        return a