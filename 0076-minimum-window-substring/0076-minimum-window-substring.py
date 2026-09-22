from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c=0
        start=0
        n=Counter(t)
        l=0
        min_len=float("inf")
        for r in range(len(s)):
            if s[r] in n:
                n[s[r]]-=1
                if n[s[r]]>=0:
                    c+=1
            while c==len(t):
                if r-l+1<min_len:
                    min_len=r-l+1
                    start=l
                if s[l] in n:
                    n[s[l]]+=1
                    if n[s[l]] >0:
                        c-=1

                l+=1

        if min_len==float('inf'):
            return ""
        return s[start:start+min_len]