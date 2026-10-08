class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def back(s,l,r,ind,bal,ans):
            if bal<0:
                return
            if ind==len(s):
                if l==0 and r==0 and bal==0:
                    ans.append(s)
                return
            if l<0 or r<0:
                return
            if s[ind]=='(' :
                back(s,l,r,ind+1,bal+1,ans)
            elif s[ind]==')' :
                back(s,l,r,ind+1,bal-1,ans)
            else:
                back(s,l,r,ind+1,bal,ans)
            if s[ind]=='(' and l>0:
                back(s[:ind]+s[ind+1:],l-1,r,ind,bal,ans)

            elif s[ind]==')' and r>0:
                back(s[:ind]+s[ind+1:],l,r-1,ind,bal,ans)
            return

        l=0
        r=0
        for ch in s:
            if ch=='(':
                l+=1
            elif ch==')':
                if l>0:
                    l-=1
                else:
                    r+=1
        ans=[]
        back(s,l,r,0,0,ans)
        return list(set(ans))