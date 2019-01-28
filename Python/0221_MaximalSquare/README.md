# [221. Maximal Square](https://leetcode.com/problems/maximal-square)

## Description

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

```
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```

## Solution

We create a **dp** whose size is the same as the **input**'s. The **dp** stores the edge length of the square that can be formed when **dp[i][j]** as the bottom right corner.

For the first row and the first column, we simply check if it's one because it's the largest possible edge.

For other positions, we first check if it's 1. If it is, we find the min value from its left, top, and top-left and plus one which is the edge of the square.

In the end we find the max from **dp** and square it which is the maximum area of the square in the **input**.

Time complexity: O(m * n)<br>
Space compelexity: O(m * n)

## Related Topics

[Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/), [Largest Plus Sign](https://leetcode.com/problems/largest-plus-sign/)
