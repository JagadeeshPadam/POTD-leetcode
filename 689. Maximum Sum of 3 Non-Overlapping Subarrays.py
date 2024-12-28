# Find the prefix sum of the array using k
# Find 3 non overlapping subarrays with maximum sum using prefix caluclated above
# Find the 3 indexes.

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        k_sums = [sum(nums[:k])]
        for i in range(k, n):
            k_sums.append(k_sums[-1] + nums[i] - nums[i - k])
        
        dp = {}
        
        def fun(i, cnt):
            if cnt == 3 or i > len(nums) - k:
                return 0
            
            if (i, cnt) in dp:
                return dp[(i, cnt)]
            pick = k_sums[i] + fun(i + k, cnt + 1)
            
            unpick = fun(i + 1, cnt)
            
            dp[(i, cnt)] = max(pick, unpick)
            return dp[(i, cnt)]
        
        def ans():
            i = 0
            indices = []
            
            while len(indices) < 3 and i <= n - k:
                pick = k_sums[i] + fun(i + k, len(indices) + 1)
                unpick = fun(i + 1, len(indices))
                
                if pick >= unpick:
                    indices.append(i)
                    i += k
                else:
                    i += 1 
                
            return indices
        return ans()