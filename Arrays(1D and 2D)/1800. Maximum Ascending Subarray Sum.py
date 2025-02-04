class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]  
        cs = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]: 
                cs += nums[i]
            else: 
                ans = max(ans, cs)
                cs = nums[i] 
        ans = max(ans, cs)
        return ans