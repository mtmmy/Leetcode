import unittest

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            val = nums[i]
            
            while val < len(nums) and val > 0 and val != nums[val - 1]:
                nums[i], nums[val - 1] = nums[val - 1], val
                val = nums[i]
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1        
        
        return len(nums) + 1

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(3, target.firstMissingPositive([1,2,0]))
        self.assertEqual(2, target.firstMissingPositive([3,4,-1,1]))
        self.assertEqual(1, target.firstMissingPositive([7,8,9,11,12]))
        self.assertEqual(6, target.firstMissingPositive([1,2,3,4,5]))

if __name__ == '__main__':
    unittest.main()    
        