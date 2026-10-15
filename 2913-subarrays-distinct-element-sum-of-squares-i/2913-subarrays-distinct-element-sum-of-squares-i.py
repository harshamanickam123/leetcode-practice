class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                x=nums[i:j+1]
                z=set(x)
                s+=len(z)**2
        return s