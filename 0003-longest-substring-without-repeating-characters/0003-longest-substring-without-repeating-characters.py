class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        a=0
        f={}
        for r in range(len(s)):
            f[s[r]]=f.get(s[r],0)+1
            while f[s[r]]>1:
                f[s[l]]-=1
                l+=1
            a=max(a,r-l+1)
        return a