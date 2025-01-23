class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        mapsR = {}
        mapsC = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i not in mapsR:
                        mapsR[i] = 1
                    else:
                        mapsR[i] += 1
                    if j not in mapsC:
                        mapsC[j] = 1
                    else:
                        mapsC[j] += 1
                    
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (mapsR[i] > 1 or mapsC[j] > 1):
                    count += 1
        return count