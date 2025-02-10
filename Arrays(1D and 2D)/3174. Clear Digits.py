class Solution:
    def clearDigits(self, s: str) -> str:
        ans = ''
        for char in s:
            if char.isdigit():
                ans = ans[:-1]
            else:
                ans += char
        return ans