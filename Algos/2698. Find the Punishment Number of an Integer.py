class Solution:
    def punishmentNumber(self, n: int) -> int:
        def fun(tar, sq, i, c):
            if i == len(sq):
                    return c == tar
            for j in range(i, len(sq)):
                if fun(tar, sq, j+1, c+int(sq[i:j+1])):
                    return True
            return False
            
        ans = 0
        for i in range(1, n+1):
            if fun(i, str(i*i), 0, 0):
                ans += i * i
        return ans