class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        r=[]
        s=[]
        def back(ind):
            if ind==len(nums):
                r.append(s.copy())
                return
            s.append(nums[ind])
            back(ind+1)
            s.pop()
            back(ind+1)
        back(0)
        return r