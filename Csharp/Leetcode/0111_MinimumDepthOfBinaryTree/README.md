# [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree)

## Description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```

return its minimum depth = 2.

## Solution

We can use DFS to solve this problem. In the recursive function, when a node has two children, we return the lower height plus 1; when a node has less than two children, we return the higher height plus 1. The reason we return the higher in the second case is the minimum height of the following example is 3.

```
     1
    /
   2
  /
 3
```

Because the definition of the minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node and there is no leaf at the right subtree of the root node.

The time complexity is O(n) and space complexity is O(log n).

## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) 

## Similar Questions

[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/), [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
