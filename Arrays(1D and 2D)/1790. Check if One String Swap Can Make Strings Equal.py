class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        if sorted(s1) != sorted(s2):
            return False
        n = len(s2)
        t = 0
        for i in range(n):
            if s1[i] != s2[i]:
                t += 1
        return True if t == 0 or t == 2 else False