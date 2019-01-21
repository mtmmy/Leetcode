# [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists)

## Description

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```

begin to intersect at node c1.

Notes:

- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Your code should preferably run in O(n) time and use only O(1) memory.

Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

## Solution

Solution 1:

We first firgure out the length of two lists and cut the longer one to make two lists have equal length. Hence we can simply find the intersection.

Solution 2:

We consider two lists as a cycled list. When we traverse a list and reach the end of it, we continue travese from the begining of the other list. With this approach, two pointers will meet at the intersection if it exists or reach null if it doesn't.

Time complexity: O(n)<br>Space complexity: O(1)

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) 

## Similar Questions

[Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/)
