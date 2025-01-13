class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7

        cc = [defaultdict(int) for _ in range(len(words[0]))]
        for col in range(len(words[0])):
            for word in words:
                cc[col][word[col]] += 1

        dp = {}

        def fun(i, k):
            if k == len(target):
                return 1
            if i == len(words[0]):
                return 0
            if (i, k) in dp:
                return dp[(i, k)]
            pick = 0
            if target[k] in cc[i]:
                pick = cc[i][target[k]] * fun(i + 1, k + 1)
            unpick = fun(i + 1, k)
            dp[(i, k)] = (pick + unpick) % MOD
            return dp[(i, k)]

        return fun(0, 0)