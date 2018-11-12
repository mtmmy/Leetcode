# [200. Number of Islands](https://leetcode.com/problems/number-of-islands)

## Description

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

```
Input:
11110
11010
11000
00000

Output: 1
```

Example 2:

```
Input:
11000
11000
00100
00011

Output: 3
```

## Solution

Simplely use depth-first search and a 2-d boolean array to examine how many islands. We set a nested loop to interate all indices in the array. We only concern indices with value "1" and haven't been visted. Once we hit a "1" index, we note this index visted and start depth-first search and update all adjacent "1" indces as visted. After finishing depth-first search, we count it as one more island. And we keep interating the grid and Since we have a used matrix to track visited land, once a "1" is visited, we will not start another depth-first search from it. Hence we can add up total groups of "1"s. 

Because we will not execute depth-first search on a single index twice, the time complexity is O(n). And we need an auxiliary space to record visited which has the same size with the input so that space complexity is O(n) as well.

## Related Topics

[Depth-first Search](https://leetcode.com/tag/depth-first-search/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) , [Union Find](https://leetcode.com/tag/union-find/) 

## Similar Questions

[Surrounded Regions](https://leetcode.com/problems/surrounded-regions/), [Walls and Gates](https://leetcode.com/problems/walls-and-gates/), [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/), [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/), [Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/), [Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
