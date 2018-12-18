# [67. Add Binary](https://leetcode.com/problems/add-binary)

## Description

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

```
Input: a = "11", b = "1"
Output: "100"
```

Example 2:

```
Input: a = "1010", b = "1011"
Output: "10101"
```

## Solution

First, reverse the character arrays so that they can align on the first place which makes us easier to sum up digit by digit. Sum up two numbers digit by digit and remember carry over to the next place if there is a carryover. Reverse back to the correct number.

We need character arrays to store reversed numbers, so the space complexity is O(n). We use a loop to sum up two numbers bit by bit, and the executing time of the loop depends on the longer number. The time complexity is O(n). And we also have 3 reversing steps. The time complexity of resersing is O(n) as well. So the total time complexity is still O(n).

## Related Topics

[Math](https://leetcode.com/tag/math/) , [String](https://leetcode.com/tag/string/) 

## Similar Questions

[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/), [Multiply Strings](https://leetcode.com/problems/multiply-strings/), [Plus One](https://leetcode.com/problems/plus-one/)
