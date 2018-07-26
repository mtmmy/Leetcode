class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * m for _ in range(n)]
        for i in range (n):
            for j in range (m):
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
        
if __name__ == "__main__":
    target = Solution()
    result = target.uniquePaths(7, 3)
    print(result)