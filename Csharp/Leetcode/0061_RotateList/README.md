# [61. Rotate List](https://leetcode.com/problems/rotate-list)

## Description

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```

Example 2:

```
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```

## Solution

First, we want to know how many nodes in the list. Because for a 5-node list, the results after rotating of k = 1, 6, 16, 1006 are all the same because their remainder of being divided by 5 are all 1. After doing modulo, we can know the fewest moves (k') we need. We set two pointers and let the **leading** pointer goes k' steps ahead of the **tracking** pointer. Then two pointers keep going forward until the **leading** one hits the end of the list. At this moment, the tracking point will be the node that is right before the head after rotating. Now we already know the new head, we can easily reorganize the list and return the rotated list.

The counting part takes n steps and finding new head takes n steps as well. Hence, we need 2n steps totally and the time complexity is O(n). We need only constant space.

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 

## Similar Questions

[Rotate Array](https://leetcode.com/problems/rotate-array/), [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/)
