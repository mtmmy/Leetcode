# [136. Single Number](https://leetcode.com/problems/single-number)

## Description

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

```
Input: [2,2,1]
Output: 1
```

Example 2:

```
Input: [4,1,2,1,2]
Output: 4
```

## Solution

We can use XOR because two same numbers operated by XOR will become 0. Also XOR has commutative property which means the results of following two fomula are the same:

```
2 ^ 2 ^ 1 = 1
1 ^ 2 ^ 2 = 1
```

So we just do XOR from the first number of the list all the way down to the last, and the result is our answer.

The time complexity is O(n) and space complexity is O(1).

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Bit Manipulation](https://leetcode.com/tag/bit-manipulation/) 

## Similar Questions

[Single Number II](https://leetcode.com/problems/single-number-ii/), [Single Number III](https://leetcode.com/problems/single-number-iii/), [Missing Number](https://leetcode.com/problems/missing-number/), [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/), [Find the Difference](https://leetcode.com/problems/find-the-difference/)
