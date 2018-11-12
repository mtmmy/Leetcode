# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)

## Description

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

## Solution

We merge lists 2 by 2. For example, we have 8 lists 0 ~ 7. We merge 0 and 1, 2 and 3, and so on. The way we merged two sorted lists is in [Merge Two Sorted Lists](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0021_MergedTwoSortedList). After the first run, we get 4 merged lists 0', 1', 2', and 3' which are all sorted. And we keep doing this process in the end we have one sorted list.

Overall the while loop runs log(k) times and k is the number of lists. Every iteration we operates nk elements. Hence the time complexity is O(nk logk) and O(1) space. 

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) , [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/) , [Heap](https://leetcode.com/tag/heap/) 

## Similar Questions

[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/), [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)
