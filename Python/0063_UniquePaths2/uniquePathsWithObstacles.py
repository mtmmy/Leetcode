class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] != 1:
            obstacleGrid[0][0] = -1

        for i in range (m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and j > 0:
                    top = 0 if obstacleGrid[i - 1][j] == 1 else obstacleGrid[i - 1][j]
                    left = 0 if obstacleGrid[i][j - 1] == 1 else obstacleGrid[i][j - 1]
                    obstacleGrid[i][j] = top + left 
                elif i > 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                elif j > 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]

        return 0 if obstacleGrid[-1][-1] == 1 else -obstacleGrid[-1][-1]
        
if __name__ == "__main__":
    target = Solution()
    grid = []
    grid.append([0, 0, 0])
    grid.append([0, 1, 0])
    grid.append([0, 0, 0])
    result = target.uniquePathsWithObstacles(grid)
    print(result)