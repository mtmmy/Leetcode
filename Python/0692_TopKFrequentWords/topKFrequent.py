import unittest

from collections import Counter
from heapq import nsmallest, heappush, heappushpop

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)
        heap = [(-val, key) for key, val in counter.items()]
        largest = nsmallest(k, heap)
        return [word for val, word in largest]

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    def __lt__(self, other):
        return self.freq < other.freq or (self.freq == other.freq and self.word > other.word)

class Solution2:
    def topKFrequent(self, words, k):
        wordCounter = Counter(words)
        heap = []
        for word, freq in wordCounter.items():
            if len(heap) < k:
                heappush(heap, Pair(word, freq))
            elif heap[0].freq < freq or (heap[0].freq == freq and heap[0].word > word):
                heappushpop(heap, Pair(word, freq))
        return [pair.word for pair in sorted(heap, reverse=True)]

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = ["i", "love"]
        test = ["i", "love", "leetcode", "i", "love", "coding"]
        self.assertEqual(expected, target.topKFrequent(test, 2))

if __name__ == '__main__':
    unittest.main()
        