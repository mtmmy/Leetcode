# [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group)

## Description

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

1. Only constant extra memory is allowed.
2. You may not alter the values in the list's nodes, only nodes itself may be changed.

## Solution

The solution is: 

1. Use a dummy node as a new head of whole list
2. Go through k nodes and keep the head and the tail of these k nodes
3. If there are k nodes, reverse these k nodes and go to #4 step
4. Connect new head (old tail) to the front part of the list and new tail(old head) to the tail part of the list
5. Return dummy.next which is the new head of the new list

We go through every nodes twice. Once for counting, the other for reversing. Hence the time complexity is O(n). 

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) 

## Similar Questions

[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
