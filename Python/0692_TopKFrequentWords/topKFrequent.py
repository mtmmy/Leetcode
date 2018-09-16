import unittest

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)

        heap = [(-val, key) for key, val in counter.items()]
        largest = heapq.nsmallest(k, heap)

        return [word for val, word in largest]
        


class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = ["i", "love"]
        test = ["i", "love", "leetcode", "i", "love", "coding"]
        self.assertEqual(expected, target.topKFrequent(test, 2))

if __name__ == '__main__':
    unittest.main()
        