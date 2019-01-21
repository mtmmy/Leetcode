# [143. Reorder List](https://leetcode.com/problems/reorder-list)

## Description

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

```
Given 1->2->3->4, reorder it to 1->4->2->3.
```

Example 2:

```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```

## Solution

We still use slow and faster pointers where faster one is twice the speed of the slower one. We start both pointers from the head of the list, when the faster once reaches the end, the slower one is at the middle of the list. We need to learn wheather the number of nodes of the list is odd or even. We can get this information by checking whether the faster pointer is pointing NULL or not. If the faster is pointing the end node, the number is odd so we need move one node more for the slow because the first half need to contain one more node.

Now we have the head of he second part. First we reverse it and then we reorder two lists as asked.

Time complexity: O(n)<br>Space Complexity: O(1)

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) 