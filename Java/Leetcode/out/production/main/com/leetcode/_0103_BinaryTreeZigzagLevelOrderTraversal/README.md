# [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal)

## Description

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```



return its zigzag level order traversal as:

```
[
  [3],
  [20,9],
  [15,7]
]
```



## Solution

This problem is similar to [102. Binary Tree Level Order Traversal](https://github.com/mtmmy/Leetcode/tree/master/Java/Leetcode/src/main/java/com/leetcode/_0102_BinaryTreeLevelOrderTraversal). The differece is that the order of each layer is reversed from the adjacent layer. We can also use BFS just like in [102. Binary Tree Level Order Traversal](https://github.com/mtmmy/Leetcode/tree/master/Java/Leetcode/src/main/java/com/leetcode/_0102_BinaryTreeLevelOrderTraversal). Also we can use DFS and we use it in this problem.

We set up a traverse function with the variable called depth which denote the current layer. If the depth is odd number, we store values from left to right. Otherwise we store values from right to left.

The time complexity and space complexity are O(n).

## Related Topics

[Stack](https://leetcode.com/tag/stack/) , [Tree](https://leetcode.com/tag/tree/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) 

## Similar Questions

[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
