class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = ''
        m, n = len(s), len(part)
        for i in s:
            ans += i
            if ans[-n:] == part:
                ans = ans[:-n]
        return ans