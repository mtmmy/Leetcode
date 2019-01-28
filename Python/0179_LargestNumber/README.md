# [179. Largest Number](https://leetcode.com/problems/largest-number)

## Description

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

```
Input: [10,2]
Output: "210"
```

Example 2:

```
Input: [3,30,34,5,9]
Output: "9534330"
```

Note: The result may be very large, so you need to return a string instead of an integer.

## Solution

We use sorting to slove this problem. The rule of sorting is, the two forms of concatenation of two numbers, we put the bigger one at the front. For example, 3 and 30, there are two forms after combining, 330 and 303. Since 330 > 303, we put these two numbers in [3, 30] order. After sorting, we just concatenate all numbers.

Time complexity: O(n log n)<br>
Space complexity: O(1)

## Related Topics

[Sort](https://leetcode.com/tag/sort/) 