import unittest

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """        
        n = len(nums)
        if n == 1:
            return nums
        
        hs = {}

        for num in nums:
            if num in hs:
                hs[num] += 1
            else:
                hs[num] = 1

        hs = sorted(hs, key = hs.get, reverse = True)
        
        i, result = 0, []
        while i < k:
            result.append(hs[i])
            i += 1

        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([1, 2], target.topKFrequent([1,1,1,2,2,3], 2))
        self.assertEqual([1], target.topKFrequent([1], 1))
        self.assertEqual([1, 3], target.topKFrequent([1,1,1,2,2,3,3,3], 2))

if __name__ == '__main__':
    unittest.main()    
        