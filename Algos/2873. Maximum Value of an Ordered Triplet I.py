class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        maxval = nums[0]
        maxdf = 0
        
        for i in range(1, n):
            ans = max(ans, maxdf * nums[i])
            maxdf = max(maxdf, maxval - nums[i])
            maxval = max(maxval, nums[i])
            
        return ans