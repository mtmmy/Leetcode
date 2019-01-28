import unittest

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if k:
            n = len(nums)
            k = k % n
            reverse(0, n - 1)
            reverse(0, k - 1)
            reverse(k, n - 1)

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k:
            n = len(nums)
            k = k % n
            nums[:] = nums[n - k:] + nums[0:n - k]

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        test = [1,2,3,4,5,6,7]
        target.rotate(test, 3)
        expected = [5,6,7,1,2,3,4]
        self.assertEqual(expected, test)
        
        test = [-1,-100,3,99]
        target.rotate(test, 2)
        expected = [3,99,-1,-100]
        self.assertEqual(expected, test)

if __name__ == '__main__':
    unittest.main()