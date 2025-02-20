class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            digit = nums[i][i]
            if digit == '1':
                ans.append('0')
            else:
                ans.append('1')
        return "".join(ans)