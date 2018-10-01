# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers)

## Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```



## Solution
The soltion is just like the vertical addition. We start from the heads of two lists and sum them up and add the carry if there is. One thing we need to be care of is the condition of the while loop. Since the length of two linked list may be different, we have to keep looping if one of them is not null or we have a carry. Once the loop has finished, we get the answer of the porbplem. The time complexity is O(M+N).