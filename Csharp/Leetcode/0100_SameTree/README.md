# [100. Same Tree](https://leetcode.com/problems/same-tree)

## Description

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

```
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```

Example 2:

```
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
```

Example 3:

```
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```

## Solution

This problem can be solved by using DFS on two trees. If any nodes between two trees are different, the trees are not the same.

The time complexity is O(n) and space complexity is O(log n).

## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) 