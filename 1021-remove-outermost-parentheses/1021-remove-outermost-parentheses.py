class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        r=""
        for ch in s:
            if ch=='(':
                if c>0:
                    r+=ch
                c+=1
            elif ch==')':
                c-=1
                if c>0:
                    r+=ch
        return r
