class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        def fun(l):
            if l > high:
                return 0
            if l in dp:
                return dp[l]
            ans = 0
            if l >= low:
                ans += 1
            ans += fun(zero+l)
            ans += fun(one+l)
            dp[l] = (ans) % (10 ** 9 + 7)
            return dp[l]
        dp = {}
        return fun(0)