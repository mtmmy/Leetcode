import unittest
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n, m = len(nums), 1
        result = []
        
        for i in range(n):
            result.append(m)
            m *= nums[i]
            
        m = 1
        for i in range(n - 1, -1, -1):
            result[i] *= m
            m *= nums[i]
        
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([24, 12, 8, 6], target.productExceptSelf([1, 2, 3, 4]))
        self.assertEqual([40320,20160,13440,10080,8064,6720,5760,5040], target.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8]))

if __name__ == '__main__':
    unittest.main()