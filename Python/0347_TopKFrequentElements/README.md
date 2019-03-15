# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

## Description

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

Example 2:

```
Input: nums = [1], k = 1
Output: [1]
```

Note:

- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Solution

We first count the number of appearences of each numbers and store the result in a hash table. This step takes O(n) time. Later we generate a min heap and keep its size with k. After consuming every number in the hash, the remaining k elements in the heap is the largest k elements. This step takes O(n log k).

Time complexity: O(n log k)<br>
Space complexity: O(n)

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Heap](https://leetcode.com/tag/heap/) 

## Similar Questions

[Word Frequency](https://leetcode.com/problems/word-frequency/), [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/), [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/), [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/), [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
