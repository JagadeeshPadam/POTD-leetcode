class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, h = 0, 10**14
        while l < h:
            m = l + (h - l) // 2
            r = sum(int(sqrt(m // i)) for i in ranks)
            if r < cars:
                l = m + 1
            else:
                h = m
        return l