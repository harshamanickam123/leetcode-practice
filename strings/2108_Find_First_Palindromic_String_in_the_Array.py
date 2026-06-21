from typing import List
class Solution:
    def check(self,w:str)->bool:
        i,j=0,len(w)-1
        while i<j:
            if w[i]==w[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.check(w):
                return w
        return ""
