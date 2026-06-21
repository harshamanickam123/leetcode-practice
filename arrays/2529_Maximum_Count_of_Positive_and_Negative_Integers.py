from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        c1=0
        for i in range(len(nums)):
            if nums[i]>0:
                c+=1
            elif nums[i]==0:
                continue
            else:
                c1+=1
        x=max(c,c1)
        return x