import unittest

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coinCount = [amount + 1] * (amount + 1)
        coinCount[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    coinCount[i] = min(coinCount[i], coinCount[i - coin] + 1)
        
        return -1 if coinCount[-1] > amount else coinCount[-1]
    
    def coinChangeDFS(self, coins, amount: int) -> int:
        if not coins:
            return -1
        upperBound = amount + 1
        self.result = upperBound
        
        def dfs(remain, count, coinIdx):
            if remain < 0:
                return
            if count - (-remain // coins[coinIdx]) > self.result:
                return
            if remain % coins[coinIdx] == 0:
                self.result = min(self.result, count + remain // coins[coinIdx])
            if coinIdx == len(coins) - 1:
                return
            for i in range((remain // coins[coinIdx]), -1, -1):
                dfs(remain - i * coins[coinIdx], count + i, coinIdx + 1)
        
        coins.sort(reverse=True)
        dfs(amount, 0, 0)
        return -1 if self.result >= upperBound else self.result

        

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(-1, target.coinChangeDFS([2], 3))
        self.assertEqual(3, target.coinChangeDFS([1,2,5], 11))
        
if __name__ == '__main__':
    unittest.main()
        