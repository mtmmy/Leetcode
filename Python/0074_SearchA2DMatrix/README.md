# [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix)

## Description

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Example 1:

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
```

Example 2:

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```

## Solution

A straightforward is search the first column first and once find the largest smaller number, search the corresponding row. Simple searching takes O(m+n).

We can reduce the time complexity to O(logM + logN) by applying binary search for those searchings.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Binary Search](https://leetcode.com/tag/binary-search/) 

## Similar Questions

[Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
