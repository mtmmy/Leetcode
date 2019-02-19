import unittest

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        for i in range(len(nums)):
            left, right = 0, len(LIS)
            while left < right:
                mid = left + (right - left) // 2
                if LIS[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if right >= len(LIS):
                LIS.append(nums[i])
            else:
                LIS[right] = nums[i]
        return len(LIS)

    def lengthOfLIS_DP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        dp = [1] * n
        result = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(4 , target.lengthOfLIS([10,9,2,5,3,7,101,18]))
        self.assertEqual(6 , target.lengthOfLIS([10,22,9,33,21,50,41,60,80]))
        
if __name__ == '__main__':
    unittest.main()
        