class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                dic[nums[i] * nums[j]] = dic.get(nums[i] * nums[j], 0) + 1
        ans = 0
        for val in dic.values():
            ans += 8 * ((val * (val - 1)) // 2)
        return ans