import unittest

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # nums.append(0)
        # n = len(nums)
        # for i in range(n):
        #     if nums[i]<0 or nums[i] >= n:
        #         nums[i]=0
                
        # for i in range(n):
        #     nums[nums[i] % n] += n

        # for i in range(1, n):
        #     if nums[i] // n == 0:
        #         return i
        # return n
        n = len(nums)
    
        for i in range(n):
            val = nums[i]
            # Swap until i matches index i - 1 (zero indexing so we can use the array as is)
            while val > 0 and val < n and val != nums[val - 1]:
                self.swap(nums, i, val)
                val = nums[i]
            
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
            
        return n + 1
    
    def swap(self, nums, i, val):
        nums[i], nums[val - 1] = nums[val - 1], val

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
        