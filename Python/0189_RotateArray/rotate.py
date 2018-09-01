import unittest

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums and k % len(nums) != 0:
            # n, start, i, cur, count = len(nums), 0, 0, nums[0], 0

            # while count < n:
            #     i = (i + k) % n
            #     temp = nums[i]
            #     nums[i] = cur
            #     if i == start:
            #         start += 1
            #         i += 1
            #         cur = nums[i]
            #     else:
            #         cur = temp
            #     count += 1
            n = len(nums)
            k = k % len(nums)
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