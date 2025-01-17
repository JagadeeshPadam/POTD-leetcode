class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        f, l = 0, 0
        for i in derived:
            if i:
                l = ~l
        return f == l