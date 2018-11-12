# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)

## Description

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

## Solution

We use to pointers. The first pointer take n steps first. After that, both pointers go foward together. Once the first pointer reaches the end of the linked list, the second pointer will point exactly on the n-th nodes from end of list, and we simply elimilate it. The time complexity is O(n) and we only need constant space.

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 