# [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii)

## Description

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

Given target = 5, return true.

Given target = 20, return false.

## Solution

Solution 1:

For each row we run the binary search and return True if we find the target. Otherwise return False at the end of the algorithm.

Let's say the matrix has m rows and n columns:<br>
Time complexity: O(m log n)<br>
Space complexity: O(1)

Solution 2:

We start at row = 0 and column = n - 1, and 

```
if matrix[row][col] == target:
    return True
elif matrix[row][col] > target:
    col -= 1
elif matrix[row][col] < target:
    row += 1
```

because if the target is smaller, it must be at the left side of columns. If the target is greater, if must be at the bottom side of rows.

Time complexity: O(m + n)<br>
Space complexity: O(1)

## Related Topics

[Binary Search](https://leetcode.com/tag/binary-search/) , [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/) 

## Similar Questions

[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
