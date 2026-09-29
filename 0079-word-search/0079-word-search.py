class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        sol=[[0]*m for i in range(n)]
        def back(i,j,sol,ind):
            if i<0 or i>=n or j<0 or j>=m or sol[i][j]==True:
                return False
            if board[i][j]!=word[ind]:
                return False
            if ind==len(word)-1:
                return True
            sol[i][j]=True
            if back(i+1,j,sol,ind+1):
                return True
            if back(i,j+1,sol,ind+1):
                return True
            if back(i-1,j,sol,ind+1):
                return True
            if back(i,j-1,sol,ind+1):
                return True
            sol[i][j]=False
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if back(i,j,sol,0):
                        return True
                
        return False
