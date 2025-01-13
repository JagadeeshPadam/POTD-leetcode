class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = ' '.join(words)
        ans = [i for i in words if s.count(i) >= 2]
        return ans