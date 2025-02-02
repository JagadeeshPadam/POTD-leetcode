class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] > nums[(i+1) % n]:
                c += 1
        return c <= 1