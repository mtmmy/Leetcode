# [62. Unique Paths](https://leetcode.com/problems/unique-paths)

## Description

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![image](https://leetcode.com/static/images/problemset/robot_maze.png)

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

Example 2:

```
Input: m = 7, n = 3
Output: 28
```

## Solution

We create a 2d-array **dp** where **dp[i][j]** stores possibile ways from start to the position **(i, j)**. Because the robot can only go right or down, the robot can only reach **(i, j)** from **(i-1, j)** or **(i, j-1)**. Hence the possible ways of reaching **(i, j)** is the sum of the possible ways of **(i-1, j)** and **(i, j-1)**. Accroding to this algorithm, we can figure out How many possible unique paths from start to finish.

The time complexity and space complexity are both O(m * n).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Unique Paths II](https://leetcode.com/problems/unique-paths-ii/), [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/), [Dungeon Game](https://leetcode.com/problems/dungeon-game/)
