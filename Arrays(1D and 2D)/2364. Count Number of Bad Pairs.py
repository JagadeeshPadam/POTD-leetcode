class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n * (n - 1)
        c = Counter(i - n for i, n in enumerate(nums))
        
        for v in c.values():
            if v > 1:
                ans -= v * (v-1)
        return ans // 2