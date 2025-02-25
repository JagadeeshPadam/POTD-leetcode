class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        oc, ec, = 0, 1
        tsum = 0
        ans = 0
        for i in arr:
            tsum += i
            if tsum % 2 == 0:
                ans += oc
                ec += 1
            else:
                ans += ec
                oc += 1
        return ans