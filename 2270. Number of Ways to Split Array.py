class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        f, r = 0, sum(nums)
        for i in range(n-1):
            f += nums[i]
            r -= nums[i]
            if f >= r:
                ans += 1
        return ans