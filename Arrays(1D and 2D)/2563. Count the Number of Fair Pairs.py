class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        def count(t):
            i, j = 0, len(nums) - 1
            res = 0

            while i < j:
                if nums[i] + nums[j] > t:
                    j -= 1
                else:
                    res += j - i
                    i += 1

            return res

        nums.sort()

        return count(upper) - count(lower - 1)