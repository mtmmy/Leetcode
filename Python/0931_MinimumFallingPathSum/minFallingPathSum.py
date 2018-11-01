class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """        
        dp = [[0] * len(A) for _ in range(len(A))]
        
        for j in range(len(A)):
            dp[0][j] = A[0][j]
        
        for i in range(1, len(A)):
            for j in range(len(A)):
                if j == 0:
                    dp[i][j] = min(A[i][j] + dp[i - 1][j], A[i][j] + dp[i - 1][j + 1])
                elif j == len(A) - 1:
                    dp[i][j] = min(A[i][j] + dp[i - 1][j], A[i][j] + dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(A[i][j] + dp[i - 1][j], A[i][j] + dp[i - 1][j - 1], A[i][j] + dp[i - 1][j + 1])

        return min(dp[-1])