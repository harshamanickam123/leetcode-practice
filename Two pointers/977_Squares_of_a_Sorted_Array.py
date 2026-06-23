from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        k=r
        a=[0]*len(nums)
        while l<=r:
            if nums[l]*nums[l]>nums[r]*nums[r]:
                a[k]=nums[l]*nums[l]
                l+=1
            else:
                a[k]=nums[r]*nums[r]
                r-=1
            k-=1
        return a