class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans=""
        a=sorted(strs)
        f=a[0]
        l=a[-1]
        for i in range(min(len(f),len(l))):
            if f[i]!=l[i]:
                return ans
            ans+=f[i]
        return ans