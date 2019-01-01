# [89. Gray Code](https://leetcode.com/problems/gray-code)

## Description

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

```
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
```

Example 2:

```
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
```

## Solution

```
00 -> 01 -> 11 -> 12
 0     1     3     2
```
Let's take a look at this example. We can observe when we divide it at the point between 1 and 3, 3 = 1 + 2 and 2 = 0 + 2.

```
000 -> 001 -> 011 -> 010 -> 110 -> 111 -> 101 -> 100
  0      1      3      2      6      7      5      4
```
Futhermore, in this example, 6 = 2 + 4, 7 = 3 + 4, 5 = 1 + 4, and 4 = 0 + 4.

Thus we can use this pattern to generate the result. The implementation is in the sourcecode. The time complexity and auxiliary space are O(2<sup>N</sup>).


## Related Topics

[Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/)
