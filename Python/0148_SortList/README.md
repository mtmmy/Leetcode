# [148. Sort List](https://leetcode.com/problems/sort-list)

## Description

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

```
Input: 4->2->1->3
Output: 1->2->3->4
```

Example 2:

```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

## Solution

We just implement merge sort. Generally merge sort needs O(n) space. However the problem gives us the linked list, so we don't need to create tmmperally space. We can just order nodes in sorted order. 

Time complexity: O(n log n)<br>Space Complexity: constant

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) , [Sort](https://leetcode.com/tag/sort/) 

## Similar Questions

[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/), [Sort Colors](https://leetcode.com/problems/sort-colors/), [Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)
