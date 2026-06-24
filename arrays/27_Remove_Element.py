from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         i=0
         j=len(nums)-1
         while i<=j:
             if val==nums[i]:
                 nums[i]=nums[j]
                 j-=1
             else:
                 i+=1
         return j+1