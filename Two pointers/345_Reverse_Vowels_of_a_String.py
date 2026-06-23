class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r,m=0,len(s)-1,list(s)
        a=set("aeiouAEIOU")
        while l<r:
            if s[l] not in a:
                l+=1
            elif s[r] not in a:
                r-=1
            else:
                m[l],m[r]=m[r],m[l]
                l+=1
                r-=1
        return "".join(m)
