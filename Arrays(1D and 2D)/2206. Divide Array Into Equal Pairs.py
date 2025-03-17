class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hshmap = {}
        for i in nums:
            hshmap[i] = hshmap.get(i, 0) + 1
        for i in hshmap:
            if hshmap[i] % 2 == 1:
                return False
        return True