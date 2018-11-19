# [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers)

## Description

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

```
Input: dividend = 10, divisor = 3
Output: 3
```

Example 2:

```
Input: dividend = 7, divisor = -3
Output: -2
```

Note:

1. Both dividend and divisor will be 32-bit signed integers.
2. The divisor will never be 0.
3. Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2<sup>31</sup>,  2<sup>31</sup> − 1]. For the purpose of this problem, assume that your function returns 2<sup>31</sup> − 1 when the division result overflows.

## Solution

The division is basicly a series substraction. For example, 11 divided by 2, we can implement by keep substrac until the result is smaller then the divisor and totol times of substractions is the quotient. However we can not use a loop to solve the problem because it may take too much time. To reduce running time, we try to substract as much as we can. We keep shifting the divsor right in bit-wise operation until the divisor is greater than the dividend. Shifting right a bit is multiplying by 2. For example, we shift a number to right with 2 bits, we get four times of the number. We also use another variable which is the quotient of dividend dividing by 2<sup>n</sup> times of the divisor where n is total shifting bits. And we substract dividend by 2<sup>n</sup> times of the divisor and start the next interation. 

## Related Topics

[Math](https://leetcode.com/tag/math/) , [Binary Search](https://leetcode.com/tag/binary-search/) 