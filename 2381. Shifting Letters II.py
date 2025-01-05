class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        sum_shift = 0
        v = [0] * (n + 1)
        
        for shift in shifts:
            l, r, direction = shift
            if direction == 0:
                v[l] -= 1
                v[r + 1] += 1
            else:
                v[l] += 1
                v[r + 1] -= 1
        
        for i in range(n):
            sum_shift += v[i]
            k = sum_shift % 26
            p = (ord(s[i]) - ord('a') + k + 26) % 26
            s = s[:i] + chr(ord('a') + p) + s[i + 1:]
        
        return s