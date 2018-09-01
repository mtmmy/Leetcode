import unittest

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        if nums[left] > nums[right]:
            while left != right - 1:
                mid = (left + right) // 2
                if nums[left] < nums[mid]:
                    left = mid
                else:
                    right = mid
            return min(nums[left], nums[right])
        return nums[left]
        

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(1, target.findMin([1,2,3]))
        self.assertEqual(1, target.findMin([3,1,2]))
        self.assertEqual(0, target.findMin([4,5,6,7,8,0,1,2,3]))
        self.assertEqual(0, target.findMin([7,8,0,1,2,3,4,5,6]))
        
if __name__ == '__main__':
    unittest.main()
        