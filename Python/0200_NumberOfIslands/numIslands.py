class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0]) if grid else 0
        
        used = [[False] * n for _ in range(m)]
        islands = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not used[i][j]:
                    self.sprawlIsland(grid, used, i, j)
                    islands += 1
                        
        return islands
    
    def sprawlIsland(self, grid, used, i, j):
        m = len(grid)
        n = len(grid[0])
        
        if i > 0 and grid[i - 1][j] == "1" and not used[i - 1][j]:
            used[i - 1][j] = True
            self.sprawlIsland(grid, used, i - 1, j)
        if j > 0 and grid[i][j - 1] == "1" and not used[i][j - 1]:
            used[i][j - 1] = True
            self.sprawlIsland(grid, used, i, j - 1)
        if i < m - 1 and grid[i + 1][j] == "1" and not used[i + 1][j]:
            used[i + 1][j] = True
            self.sprawlIsland(grid, used, i + 1, j)
        if j < n - 1 and grid[i][j + 1] == "1" and not used[i][j + 1]:
            used[i][j + 1] = True
            self.sprawlIsland(grid, used, i, j + 1)
        