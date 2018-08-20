import unittest
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        
        l = len(nums)
        left_arr, right_arr, left, right = [1]*l, [1]*l, 1, 1
        
        for i in range(1, l):
            left *= nums[i-1]
            left_arr[i] = left
        
        for j in range(l-2, -1, -1):
            right *= nums[j+1]
            right_arr[j] = right
        
        return [tup[0]*tup[1] for tup in zip(left_arr, right_arr)]

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([24, 12, 8, 6], target.productExceptSelf([1, 2, 3, 4]))
        self.assertEqual([40320,20160,13440,10080,8064,6720,5760,5040], target.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8]))



if __name__ == '__main__':
    unittest.main()