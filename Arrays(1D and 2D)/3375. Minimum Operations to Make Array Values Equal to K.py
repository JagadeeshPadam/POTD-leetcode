class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        lenofnumset, minimum = len(set(nums)), min(nums)
        if minimum < k: return -1
        elif minimum > k: return lenofnumset
        else: return lenofnumset - 1