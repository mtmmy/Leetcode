import unittest

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        
        return -1 if dp[amount] > amount else dp[amount]

        

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(-1, target.coinChange([2], 3))
        self.assertEqual(3, target.coinChange([1,2,5], 11))
        
if __name__ == '__main__':
    unittest.main()
        