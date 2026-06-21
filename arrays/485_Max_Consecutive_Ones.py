from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=[]
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                c=0
            l.append(c)
        return max(l)
