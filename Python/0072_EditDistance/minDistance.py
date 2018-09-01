import unittest

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        h, w = len(dp), len(dp[0])

        for i in range(h):
            dp[i][0] = i
        for j in range(w):
            dp[0][j] = j

        for i in range(1, h):
            for j in range(1, w):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:                    
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
        return dp[-1][-1]


class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(3 , target.minDistance("horse", "ros"))
        self.assertEqual(5 , target.minDistance("intention", "execution"))
        
if __name__ == '__main__':
    unittest.main()
        