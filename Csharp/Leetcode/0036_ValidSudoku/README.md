# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku)

## Description

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

```
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```

Example 2:

```
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

Note:

## Solution

Use three map which is good at searching elements to store states of numbers in rows, columns and sub-boxes. We go over the board and whenever we get a number, we check if this number has existed in the same row, column or sub-box. If the same number exists, the program returns false. Otherwise, we add the number to the corespoding row, column and sub-box.
        
Since we only go over the board once, the time complexity is O(n). However we need extra space to store states for rows, columns and sub-boxes and the space complexity is O(n). 

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) 

## Similar Questions

[Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
