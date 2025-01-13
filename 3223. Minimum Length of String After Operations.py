class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        ans = 0
        freq = Counter(s)
        for d in freq:
            key, val = d, freq[d]
            ans += (val - 1) if val % 2 == 1 else val - 2
        return n - ans