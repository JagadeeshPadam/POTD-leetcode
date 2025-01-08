class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # words.sort(key = lambda x: len(x))
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans += 1
        return ans