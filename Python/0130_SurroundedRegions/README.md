# [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions)

## Description

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

```
X X X X
X O O X
X X O X
X O X X
```

After running your function, the board should be:

```
X X X X
X X X X
X X X X
X O X X
```

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

## Solution

From the example we can see only circles that on the edge of the board or circles that connect to edge through other circles are not surronded. So we can start from circles on the edge and find all circles that it connects with and mark them another character. (Here we use "a".). After this step, only circles that are surronded are still shown as circles. The last thing we have to do is convert circles to crosses and convert "a" back to circles.

The time complexity is O(n) where is combined from the converting not sorrunded circles to "a" which takes O(n) and the converting surronded circles to corsses and converting "a" back to circles which also takes O(n). n is the number of elements in the board. And the space complexity is O(1) since we update in place. 

## Related Topics

[Depth-first Search](https://leetcode.com/tag/depth-first-search/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) , [Union Find](https://leetcode.com/tag/union-find/) 

## Similar Questions

[Number of Islands](https://leetcode.com/problems/number-of-islands/), [Walls and Gates](https://leetcode.com/problems/walls-and-gates/)
