class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) if grid else 0
        
        used = [[False] * n for _ in range(m)]
        islands = 0
        
        def sprawlIsland(i, j):
            if i > 0 and grid[i - 1][j] == "1" and not used[i - 1][j]:
                used[i - 1][j] = True
                sprawlIsland(i - 1, j)
            if j > 0 and grid[i][j - 1] == "1" and not used[i][j - 1]:
                used[i][j - 1] = True
                sprawlIsland(i, j - 1)
            if i < m - 1 and grid[i + 1][j] == "1" and not used[i + 1][j]:
                used[i + 1][j] = True
                sprawlIsland(i + 1, j)
            if j < n - 1 and grid[i][j + 1] == "1" and not used[i][j + 1]:
                used[i][j + 1] = True
                sprawlIsland(i, j + 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not used[i][j]:
                    sprawlIsland(i, j)
                    islands += 1
                        
        return islands
        