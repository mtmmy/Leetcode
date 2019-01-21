class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pathCount = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, used, steps):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            elif used[i][j]:
                return                  
            elif grid[i][j] == 0:
                used[i][j] = True                
                dfs(i - 1, j, [row[:] for row in used], steps - 1)
                dfs(i + 1, j, [row[:] for row in used], steps - 1)
                dfs(i, j - 1, [row[:] for row in used], steps - 1)
                dfs(i, j + 1, [row[:] for row in used], steps - 1)
            elif grid[i][j] == -1 or grid[i][j] == 1:
                return
            else:
                if steps == 0:
                    nonlocal pathCount
                    pathCount += 1

        used = [[False] * n for _ in range(m)]
        steps = sum([row.count(0) for row in grid])     # zeros in the grid
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    used[i][j] = True
                    dfs(i - 1, j, [row[:] for row in used], steps)
                    dfs(i + 1, j, [row[:] for row in used], steps)
                    dfs(i, j - 1, [row[:] for row in used], steps)
                    dfs(i, j + 1, [row[:] for row in used], steps)

        return pathCount