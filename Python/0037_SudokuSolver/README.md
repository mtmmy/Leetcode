# [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver)

## Description

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

A sudoku puzzle...

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

...and its solution numbers marked in red.

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)

Note:

- The given board contain only digits 1-9 and the character '.'.
- You may assume that the given Sudoku puzzle will have a single unique solution.
- The given board size is always 9x9.

## Solution

We use DFS to try out every possible number in each unassigned slot. If the number is valid (for row, column, and sub-box), we assgin the number and go to the next unassigned slot. Otherwise, we reset the slot to "." (unassigned) and roll back to the previous assigned slot. By following this procedure, we end up with a fully assigned Soduku board if there is a solution.

The time complexity of this algorithm is O(9<sup>m</sup>) where m is the number of blank slots. This is because we need try each number between 1 and 9 for each blank slots. Fortunately, the amount of blank slots will never exceed 81 and we only need one solution. So the real execution time will be significant less than O(9<sup>m</sup>).

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
