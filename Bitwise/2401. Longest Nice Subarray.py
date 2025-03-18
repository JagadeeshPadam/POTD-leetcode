class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used, j, ans = 0, 0, 0
        for i in range(len(nums)):
            while used & nums[i] != 0:
                used ^= nums[j]
                j += 1
            used |= nums[i]
            ans = max(ans, i-j+1)
        return ans