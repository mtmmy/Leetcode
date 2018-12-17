# [48. Rotate Image](https://leetcode.com/problems/rotate-image)

## Description

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

```
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

Example 2:

```
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

## Solution

Let's use this matrix as an example. We start with the top-left corner and at this point, we need rotate four numbers on four coners, 5 to 11, 11 to 16, 16 to 15 and 15 to 5. So we use a SwapFour function to accomplish this task. In the main body of the solution, we use a nested loop to visit each starting point of SwapFour function. However we don't need to go over all matrix. In this, example, we only need to visit, 5, 1, 9, 4 because the top-right corner (whose value is 11) has been updated when the starting point is the top-left corner.

The time complexity of the algorithm is O(n<sup>2</sup>) where n is the dimensions of the matrix and we only need constant space.

## Related Topics

[Array](https://leetcode.com/tag/array/) 