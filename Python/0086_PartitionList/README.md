# [86. Partition List](https://leetcode.com/problems/partition-list)

## Description

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

```
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
```

## Solution

We create two dummy heads of linked lists for smaller numbers and graeter or equal numbers. And we go through the original linked list, and assign each nodes depending on their value. In the end we simply connect the end of the smaller list to the head of the greater list.

The time complexity is O(N) and auxiliary space is O(1).

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 