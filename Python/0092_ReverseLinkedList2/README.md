# [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii)

## Description

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

```
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
```

## Solution

We can divide a list into three part. The first and the third part remain unchanged and reverse the second part. We start at go through (m - 1) steps and keep the end node of the first part and the starting node of the second part (will become the end of the second part after reverse). Then we start reverse the node at the second part with (n - m) steps. Now we reach the starting point of the third part and we also know the end of the second part. We simply link the end of the first part to the end of the second part (head after reverse), and connect the starting nod of the second part to the starting noe of the third part and we are done.

The time complexity is O(N) because we go through the list just once. The auxiliary space is O(1).


## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) 

## Similar Questions

[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
