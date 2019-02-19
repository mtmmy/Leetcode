# [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list)

## Description

Given a singly linked list, determine if it is a palindrome.

Example 1:

```
Input: 1->2
Output: false
```

Example 2:

```
Input: 1->2->2->1
Output: true
```

Follow up:
Could you do it in O(n) time and O(1) space?

## Solution

Use the fast and the slow pointers to find the middle of the list and break it into two parts. Then we reverse the tail part and compare it to the head part node by node. If there are different nodes, the list is not palindrome.

Time complexity: O(n)<br>
Space complexity: O(1)

## Related Topics

[Linked List](https://leetcode.com/tag/linked-list/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 

## Similar Questions

[Palindrome Number](https://leetcode.com/problems/palindrome-number/), [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/), [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
