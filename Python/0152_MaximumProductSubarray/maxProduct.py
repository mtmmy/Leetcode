import unittest

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum
        # if not nums:
        #     return 0

        # n = len(nums)
        # if n == 1:
        #     return nums[0]

        # dp, maximum = [[1] * (n + 1) for _ in range(n)], 0
        # dp[0][0] = 1

        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         dp[i][j] = dp[i][j - 1] * nums[j - 1]
        #         maximum = max(maximum, dp[i][j])
        
        # return maximum
        
            

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(-2, target.maxProduct([-2]))
        self.assertEqual(6, target.maxProduct([2,3,-2,4]))
        self.assertEqual(96, target.maxProduct([2,3,-2,4,-2]))

if __name__ == '__main__':
    unittest.main()
        