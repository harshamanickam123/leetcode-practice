class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0

        for i in range(n):
            seen = set()
            c = 0

            for j in range(i, n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    c += 1

                s += c * c

        return s