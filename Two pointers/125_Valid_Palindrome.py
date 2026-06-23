class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=""
        for ch in s:
            if ch.isalnum():
                p+=ch
        a=p.lower()
        return a==a[::-1]