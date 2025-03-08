class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        c = 0
        for i in range(k):
            if b[i] == 'W':
                c += 1
        a, l = c, 0
        for i in range(k, len(b)):
            if b[l] == 'W':
                c -= 1
            l += 1
            if b[i] == 'W':
                c += 1
            a = min(a,c)
        return a