class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        island_sizes = {0: 0} 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        
        def dfs(i, j, id):
            if not (0 <= i < n and 0 <= j < n) or grid[i][j] != 1:
                return 0
            grid[i][j] = id 
            size = 1
            for dx, dy in directions:
                size += dfs(i + dx, j + dy, id)
            return size

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1 

        max_island = max(island_sizes.values(), default=0)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_islands = set()
                    new_size = 1 

                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen_islands.add(grid[ni][nj])
                    
                    for island in seen_islands:
                        new_size += island_sizes[island]

                    max_island = max(max_island, new_size)

        return max_island