from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            comp=target-nums[i]
            if comp in d:
                return [d[comp],i]
            d[nums[i]]=i
        return []

        