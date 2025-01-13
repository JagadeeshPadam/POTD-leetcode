class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        c = 0
        for i in d.values():
            if i % 2 == 1:
                c += 1
        return k >= c