import unittest
from collections import Counter
from heapq import heappush, heappop, nlargest

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """        
        eCounter = Counter(nums)
        heap = []
        
        for key, val in eCounter.items():
            heappush(heap, (val, key))
            if len(heap) > k:
                heappop(heap)
        result = []
        while heap:
            result.append(heappop(heap)[1])
        return result[::-1]
        # return nlargest(k, eCounter.keys(), key=eCounter.get)

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([1, 2], target.topKFrequent([1,1,1,2,2,3], 2))
        self.assertEqual([1], target.topKFrequent([1], 1))
        self.assertEqual([1, 3], target.topKFrequent([1,1,1,2,2,3,3,3], 2))

if __name__ == '__main__':
    unittest.main()    
        