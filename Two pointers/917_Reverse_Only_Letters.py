class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l,r=0,len(s)-1
        a=list(s)
        while l<r:
            if not a[l].isalpha():
                l+=1
            elif not a[r].isalpha():
                r-=1
            else:
                a[l],a[r]=a[r],a[l]
                l+=1
                r-=1
        return "".join(a)