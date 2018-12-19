# [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes)

## Description

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

```
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

Example 2:

```
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```

Follow up:

- A straight forward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?

## Solution

The O(mn) solution will be create a new matrix to store the result.

The O(m+n) solution is use two arrays denote which columns and rows should be set to zero. And use them to update the original matrix.

To implement the constant space solution, we need use the first row and the first column to keep the information for updating.
 
1. Check whether the first row or the first column need to bu update.
2. Set zero to the index that the corresponding column need to be set to zeros and do the same thing for the first column.
3. Update rows and columns who has to be updated.
4. Update the first row and the first column if needed.

We accomplished this algorithm is the given matrix, so the space complexity is constant. The time complexity is still O(mn).

## Related Topics

[Array](https://leetcode.com/tag/array/) 

## Similar Questions

[Game of Life](https://leetcode.com/problems/game-of-life/)
