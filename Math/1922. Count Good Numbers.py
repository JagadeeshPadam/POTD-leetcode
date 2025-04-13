class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        good, x, i = 5 ** (n % 2), 4 * 5, n // 2
        while i > 0:
            if i % 2 == 1:
                good = good * x % MOD
            x = x * x % MOD
            i //= 2
        return good