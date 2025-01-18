class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, 0)])
        dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        dic = {(0, 0): 0}
        while q:
            r, c, cost = q.popleft()
            if (r, c) == (m-1, n-1):
                return cost
            for d in dirs:
                dr, dc = dirs[d]
                nr, nc = r + dr, c + dc
                ncost = cost if d == grid[r][c] else cost + 1
                if not (0 <= nr < m and 0 <= nc < n) or ncost >= dic.get((nr, nc), float('inf')):
                    continue
                dic[(nr, nc)] = ncost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, ncost))
                else:
                    q.append((nr, nc, ncost))
        return -1