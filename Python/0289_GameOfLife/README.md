# [289. Game of Life](https://leetcode.com/problems/game-of-life)

## Description

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

```
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
```

Follow up:

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

## Solution

Straightforwardly, we can use another board to keep the next state. This approach costs us O(n) space and the time comlexity is O(n).

Actually we can do this in-place. We just use different number to represent the live state of the next state. In our implementation, we use 10 as the number. If the cell will live at the next state, we add 10 on it. Adding the doesn't effect its current state since we can use modulo of 10 to get its current state. After this we just divide all cell by 10 and we get the result. Time complexity remains O(n) and the auxiliary space is just O(1).

## Related Topics

[Array](https://leetcode.com/tag/array/) 

## Similar Questions

[Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
