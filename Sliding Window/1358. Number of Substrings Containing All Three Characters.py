class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = i = 0
        count = {c: 0 for c in 'abc'}
        for j in range(len(s)):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            ans += i
        return ans