import unittest

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                result.append(abs(idx + 1))
            else:
                nums[idx] = -nums[idx]
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = [2,3]
        test = [4,3,2,7,8,2,3,1]
        self.assertEqual(expected, target.findDuplicates(test))

if __name__ == '__main__':
    unittest.main()
        