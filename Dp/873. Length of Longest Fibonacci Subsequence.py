class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        ans = 0
        
        for j in range(n):
            for i in range(j):
                prev = arr[j] - arr[i]
                
                if prev < arr[i] and prev in index:
                    k = index[prev]
                    dp[(i, j)] = dp.get((k, i), 2) + 1
                    ans = max(ans, dp[(i, j)])
                else:
                    dp[(i, j)] = 2
        
        return ans if ans >= 3 else 0