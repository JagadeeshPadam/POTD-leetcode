class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if not(0 <= r < m) or not(0 <= c < n) or grid[r][c] == 0 or  (r, c) in vis:
                return 0
            vis.add((r, c))
            ans = grid[r][c]
            dirs = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            for nx, ny in dirs:
                ans += dfs(nx, ny)
            return ans

        ans = 0
        m, n = len(grid), len(grid[0])
        vis = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in vis:
                    ans = max(ans, dfs(i, j))
        return ans