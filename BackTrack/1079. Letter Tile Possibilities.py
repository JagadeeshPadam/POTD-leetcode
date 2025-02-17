class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        def fun():
            ans = 0
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    ans += 1 + fun()
                    count[c] += 1
            return ans
        return fun()