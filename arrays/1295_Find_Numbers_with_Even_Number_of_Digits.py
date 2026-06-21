from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            x=str(i)
            if len(x)%2==0:
                c+=1
        return c