class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        lo, up = lower, upper
        for diff in differences:
            lo, up = max(lower, lo + diff), min(upper, up + diff)
            if lo > upper or up < lower: return 0

        return up - lo + 1