class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        hmap = {}
        
        for i in range(m):
            for j in range(n):
                hmap[mat[i][j]] = (i, j)
        rc, cc = [0] * m, [0] * n
        
        for i in range(m*n):
            row, col = hmap[arr[i]]
            rc[row] += 1
            cc[col] += 1
            
            if rc[row] == n:
                return i
            if cc[col] == m:
                return i
                
        return -1