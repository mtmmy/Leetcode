import unittest

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])        
        used = [[False] * n for _ in range(m)]
        maxArea = -1
        for i in range(m):
            for j in range(n):
                if not used[i][j]:
                    area = self.dfs(grid, used, i, j)
                    maxArea = max(maxArea, area)
        return maxArea

    def dfs(self, grid, used, i, j):
        if grid[i][j] == 0 or used[i][j]:
            return 0
        if grid[i][j] == 1:
            used[i][j] = True
            m, n = len(grid), len(grid[0])
            area = 1
            if i > 0:
                area += self.dfs(grid, used, i - 1, j)
            if j > 0:
                area += self.dfs(grid, used, i, j - 1)
            if i < m - 1:
                area += self.dfs(grid, used, i + 1, j)
            if j < n - 1:
                area += self.dfs(grid, used, i, j + 1)
            return area
        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(8, target.maxAreaOfIsland([[1, 1, 1],[0, 1, 1],[0, 1, 0],[0, 1, 1]]))
        self.assertEqual(7, target.maxAreaOfIsland([[0, 1, 1],[0, 1, 1],[0, 1, 0],[0, 1, 1]]))

if __name__ == '__main__':
    unittest.main()    
        