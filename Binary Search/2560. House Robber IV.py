class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def fun(cap):
            i, c = 0, 0
            while i < len(nums):
                if nums[i] <= cap:
                    c += 1
                    i += 2  # Skip the next element to maintain non-adjacency
                else:
                    i += 1
                if c == k:
                    return True
            return False
        
        l, r = min(nums), max(nums)  # Fixing the search space
        ans = r

        while l <= r:
            m = (l + r) // 2
            if fun(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans
