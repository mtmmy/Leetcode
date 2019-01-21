# [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii)

## Description

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

## Solution

There is a clear figure of an example in [[LeetCode] Linked List Cycle II, Solution](http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html).

![](http://lh3.ggpht.com/-M78brPNoJO4/UpEoBaEQkbI/AAAAAAAAHtI/AswZn_boyG8/s1600-h/image%25255B3%25255D.png)

Two pointers meet at K node so that:

```
t = X + nY + K
2t = X + mY + K
(m - 2n)Y = X + K
```

Hence we know we need X more steps to go back to the starting node of the circle after two pointers met. So we use the algorithm in [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle) to find the node that two pointers meet. After that, we set a pointer at the head of the list and keep moving the slow pointer. They indeed will meet each other at the starting node of the circle.

The time complexity is O(n) and the space complexity is O(1).


## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 

## Similar Questions

[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
