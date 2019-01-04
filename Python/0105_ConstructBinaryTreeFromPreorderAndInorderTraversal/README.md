# [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)

## Description

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```

## Solution

First we need to understand the characteristics of two kinds of ordering. For Preorder, the nodes are orgnized level by level from the root and from left to right of each layer. For Inorder, the nodes of the left subtree and that of the right subtree are seperate by the current node.

Hence we use Preorder list to decide which node we are going to build and use the index of that node to create subproblems by using Inorder list. The algorithm is as follows:

1. Take out the first value in the Preorder and find its index, **idx**, in the Inorder if Inorder is not empty.
2. Build a node, **curNode**, on the value
3. Divide Inorder into two part by **idx**. The left subtree of **curNode** is built up by the left part of Inorder. The right subtree of **curNode** is built up by the right part of Inorder. Use updated Inorder and start two subproblems from step 1.
4. Return **curNode**.

The time complexity is O(n<sup>2</sup>) because for each value in Preorder, we need O(n) to find the corresponding index in Inorder. And there are n elements in Preorder. The space complexity is O(n) which is the number of nodes of the tree we build up.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) 

## Similar Questions

[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
