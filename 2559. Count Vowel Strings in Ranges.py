class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def isVowel(word: str) -> bool:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return word[0] in vowels and word[-1] in vowels

        n = len(words)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if isVowel(words[i]) else 0)

        ans = []
        for li, ri in queries:
            ans.append(prefix_sum[ri + 1] - prefix_sum[li])
        return ans