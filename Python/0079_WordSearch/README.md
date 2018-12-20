# [79. Word Search](https://leetcode.com/problems/word-search)

## Description

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

## Solution

Use dfs approach to go through the whole matrix. In the dfs function, if the level is equal to the length of the target word, it means we find the target word. If not, we check if it's valid by far. The condition of the validation is written in the soruce code. If it's valid, we goes deeper by toward to 4 directions.

Since we need check 4 directions for each level, the time complexity is O(n<sup>4</sup>k) where n is the length of the given word and k is the amount of elemnts in the board. And we need O(n) auxiliary space.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Word Search II](https://leetcode.com/problems/word-search-ii/)
