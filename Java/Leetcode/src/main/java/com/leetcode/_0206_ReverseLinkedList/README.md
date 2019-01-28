# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list)

## Description

Reverse a singly linked list.

Example:

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solution

We need two nodes to track the previous and the next one, **preNode** and **nextNode**. For every node starting from the head, we do the following steps:

```
nextNode = curNode.next;
curNode.next = preNode;
preNode = curNode;
curNode = nextNode;
```

We keep the next node, turn around the pointer to the previous node, and move to the next node.

Time complexity: O(n)<br>
Space complexity: O(1)

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) 

## Similar Questions

[Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/), [Binary Tree Upside Down](https://leetcode.com/problems/binary-tree-upside-down/), [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
