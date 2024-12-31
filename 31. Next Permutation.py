class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        x = n - 2
        # Step 1: Find the first decreasing element from the right
        while x >= 0 and nums[x] >= nums[x + 1]:
            x -= 1
        if x >= 0:
            # Step 2: Find the element just larger than nums[x] to the right of it
            l = n - 1
            while l > x and nums[l] <= nums[x]:
                l -= 1
            # Step 3: Swap the two elements
            nums[x], nums[l] = nums[l], nums[x]
        # Step 4: Reverse the subarray to the right of x
        nums[x + 1:] = reversed(nums[x + 1:])
