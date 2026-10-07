class Solution:

    def back(self,s,ind,left,right,bal,ans):

        # 1. INVALID

        if bal<0:
            return

        # 2. GOAL

        if ind==len(s):

            if left==0 and right==0 and bal==0:
                ans.add(s)

            return

        # 3. PRUNE

        if left<0 or right<0:
            return

        # 4. INCLUDE

        if s[ind]=='(':

            self.back(s,ind+1,left,right,bal+1,ans)

        elif s[ind]==')':

            self.back(s,ind+1,left,right,bal-1,ans)

        else:

            self.back(s,ind+1,left,right,bal,ans)

        # 5. EXPLORE

        if s[ind]=='(' and left>0:

            self.back(
                s[:ind]+s[ind+1:],
                ind,
                left-1,
                right,
                bal,
                ans
            )

        elif s[ind]==')' and right>0:

            self.back(
                s[:ind]+s[ind+1:],
                ind,
                left,
                right-1,
                bal,
                ans
            )

        # 6. UNDO

        # no undo because string is immutable

        # 7. TRY NEXT

        # recursion handles it

        # 8. RETURN

        return


    def removeInvalidParentheses(self,s):

        left=0
        right=0

        for ch in s:

            if ch=='(':

                left+=1

            elif ch==')':

                if left>0:
                    left-=1

                else:
                    right+=1

        ans=set()

        self.back(s,0,left,right,0,ans)

        return list(ans)