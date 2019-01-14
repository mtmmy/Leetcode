# [120. Triangle](https://leetcode.com/problems/triangle)

## Description

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

## Solution

We create the sampe shape of the input triangle and each element stores the smallest possible sum from the peak. Use the given example to illustrate:

```
[
     [2],
    [5,6],
  [11,10,13],
 [15,11,18,16]
]
```

The time complexity and the space complexity are O(n) where n is the total amount of numbers in the input triangle.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 