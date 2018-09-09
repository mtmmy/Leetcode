import unittest

class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones: 
            return False
        n = len(stones)
        jumpMap= {key: set() for key in range(n)}
        dp = [0] * n
        jumpMap[0].add(0)
        
        k = 0
        for i in range(1, n):
            while dp[k] + 1 < stones[i] - stones[k]:
                k += 1
            for j in range(k, i):
                distance = stones[i] - stones[j]
                
                if (distance - 1) in jumpMap[j] or distance in jumpMap[j] or (distance + 1) in jumpMap[j]:
                    jumpMap[i].add(distance)
                    dp[i] = max(dp[i], distance)
        return dp[-1] > 0
        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = False
        test = [0,1,3,5,8,9]
        self.assertEqual(expected, target.canCross(test))
        expected = False
        test = [0,1,2,3,4,8,9,11]
        self.assertEqual(expected, target.canCross(test))

if __name__ == '__main__':
    unittest.main()
        