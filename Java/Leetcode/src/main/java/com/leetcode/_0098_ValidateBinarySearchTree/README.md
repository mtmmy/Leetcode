# [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)

## Description

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:

```
Input:
    2
   / \
  1   3
Output: true
```

Example 2:

```
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
```

## Solution

According to the given definition, we can set up a simple recursive function with variables **max** and **min**. We replace the max value by the value of the current node when we go to the left subtree and replace the min value by the value of the current node when we go to the right subtree. During the recursion, if there is a node who violates its boundry, then we know the tree is not a valid BST.

The time complexity is O(n) and the space complexity is O(log n) where n is the number of nodes of the BST.


## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) 

## Similar Questions

[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/), [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)
