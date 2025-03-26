class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        result = float("Inf")
        nrow = len(grid)
        ncol = len(grid[0])
        nums = []
        dp = [0] * (nrow * ncol)

        for r in range(nrow):
            for c in range(ncol):
                nums.append(grid[r][c])

        nums.sort()
        
        for i in range(len(nums) - 1):
            diff = nums[i+1] - nums[i]
            if diff % x != 0:
                return -1
            else:
                dp[i+1] = dp[i] + ((diff // x) * (i+1))

        ops = 0        
        for i in reversed(range(1, len(dp))):
            ops += ((nums[i] - nums[i-1]) // x) * (len(nums) - i)
            result = min(result, ops + dp[i-1])
   
        if result == float("Inf"):
            return 0
        else:
            return result