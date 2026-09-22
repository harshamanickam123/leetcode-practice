class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f={}
        l=0
        a=0
        for r in range(len(s)):
            f[s[r]]=f.get(s[r],0)+1
            while (r-l+1)- max(f.values()) > k:
                f[s[l]]-=1
                l+=1
            a=max(a,r-l+1)
        return a