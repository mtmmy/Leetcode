# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)

## Description

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

Example 2:

```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

## Solution

We maintain a min heap with size **k** and go through the **input** and insert the number once the number is greater than the smallest number in the heap.

Time complexity: O(n log n)<br>
Space complexity: O(k)

## Related Topics

[Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/) , [Heap](https://leetcode.com/tag/heap/) 

## Similar Questions

[Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/), [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/), [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/), [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
