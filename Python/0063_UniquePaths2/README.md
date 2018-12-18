# [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii)

## Description

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![image](https://leetcode.com/static/images/problemset/robot_maze.png)



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

## Solution

We can use the same algorithm from [62. Unique Paths](https://github.com/mtmmy/Leetcode/tree/master/Python/0062_UniquePaths). However, in the given board it use **1** as obstacles. So here we use a little trick, we calculate paths by negative numbers and convert it to positive number when returning.

The algorithm is very similar to the one we use to solve [62. Unique Paths](https://github.com/mtmmy/Leetcode/tree/master/Python/0062_UniquePaths). What we need to do here is to ignore obstacle elements.

The time complexity here is O(N) where N is the size of the given board and we just need constant space since the board has been given.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Unique Paths](https://leetcode.com/problems/unique-paths/)
