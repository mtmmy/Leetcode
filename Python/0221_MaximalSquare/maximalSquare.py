import unittest

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            
        for i in range(1, m):
            dp[i][0] = int(matrix[i][0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":                    
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return max(map(max, dp)) ** 2

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = 4
        test = [4,3,2,7,8,2,3,1]
        self.assertEqual(expected, target.maximalSquare(test))

if __name__ == '__main__':
    unittest.main()
        