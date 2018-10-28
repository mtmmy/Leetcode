# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists)

## Description

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```



## Solution

First we have to select the head of the merged linked list which is the smaller one of two heads from each linked list. After that we iterate on both linked list and keep adding the smaller one to the new linked list, which is basic the procedure when we do the merging process in the merge sort.

The time complexity of this solution is O(m+n) where m and n are elements of two linked list.