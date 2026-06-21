from typing import List
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        a=""
        while i<len(word1) and j<len(word2):
            a+=word1[i]
            a+=word2[j]
            i+=1
            j+=1
        while i<len(word1):
            a+=word1[i]
            i+=1
        while j<len(word2):
            a+=word2[j]
            j+=1
        return "".join(a)