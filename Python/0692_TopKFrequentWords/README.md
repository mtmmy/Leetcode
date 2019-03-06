# [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words)

## Description

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```

Example 2:

```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```

Note:

1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
2. Input words contain only lowercase letters.

Follow up:

1. Try to solve it in O(n log k) time and O(n) extra space.

## Solution

Solution 1:

We create a heap with the size n and pop k smallest elements. Since we have n elements and create a heap with size n, it totally takes O(n log n) time.

Time complexity: O(n log n)<br>
Space complexity: O(n)

```
counter = Counter(words)
heap = [(-val, key) for key, val in counter.items()]
largest = nsmallest(k, heap)
return [word for val, word in largest]
```

Solution 2:

We still use heap. The different is this time we only create a heap with size k. Hence we need to declare a class with a costomized less than function.

Time complexity: O(n log n)<br>
Space complexity: O(n)

```
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
```

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Heap](https://leetcode.com/tag/heap/) , [Trie](https://leetcode.com/tag/trie/) 

## Similar Questions

[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
