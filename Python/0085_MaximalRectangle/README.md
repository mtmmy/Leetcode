# [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle)

## Description

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

```
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

## Solution

We first create a list two track the height of each column. The definition of the height is the number of consective "1" at the specific row of the column. Here we use a trick which is adding an extra column at the last in order to help us to calculate rectangles reach the right edge of the matrix.

Now for each row, we have the height of each column. This is the same problem as [84. Largest Rectangle in Histogram](https://github.com/mtmmy/Leetcode/tree/master/Python/0084_LargestRectangleInHistogram). By using the same algorithm, we can calcuate maximum rectangle at each row, which also means we can find the maximum rectangle of the matrix.

Let's say the height and the width of the matrix is M and N respectively, the time complexity of this algorithm is O(M*N) and auxiliary space is O(N).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Hash Table](https://leetcode.com/tag/hash-table/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) , [Stack](https://leetcode.com/tag/stack/) 

## Similar Questions

[Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/), [Maximal Square](https://leetcode.com/problems/maximal-square/)
