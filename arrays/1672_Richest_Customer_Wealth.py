from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        d=[]
        for a in accounts:
            t=sum(a)
            d.append(t)
        return max(d)