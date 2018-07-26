class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    minPath = min(grid[i - 1][j], grid[i][j - 1])
                    grid[i][j] += minPath
                elif i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j - 1]
        return grid[-1][-1]
        
if __name__ == "__main__":
    target = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    result = target.minPathSum(grid)
    print(result)