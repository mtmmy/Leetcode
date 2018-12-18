# [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum)

## Description

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

## Solution

The algorithm is similiar to the one of [62. Unique Paths](https://github.com/mtmmy/Leetcode/tree/master/Python/0062_UniquePaths). Because we can only go right or down, we can get the minimum path sum of (i, j) by choosing the smaller sum between (i-1, j) and (i, j-1). Using the example that the problem provides, the result of it will be as follows:

```
[
	[1, 4, 5], 
	[2, 7, 6], 
	[6, 8, 7]
]
```

So the minimum path sum is 7. The time complexity here is O(N) where N is the size of the grid and we just need constant space since the board has been given.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Unique Paths](https://leetcode.com/problems/unique-paths/), [Dungeon Game](https://leetcode.com/problems/dungeon-game/), [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/)
