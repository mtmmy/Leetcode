# [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)

## Description

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

Follow up: Recursive solution is trivial, could you do it iteratively?

## Solution

The defination of the inorder traversal is that we represent a tree in the left-self-right order. For example, we have a tree as follows:

```
   1
  / \
 4   2
    / \
   3   5
Inorder traversal: [1,4,3,2,5]   
```

We can use a stack and put the nodes in the right-self-left order. Since the stack is a FILO structure, we will get the left-self-right order when we retrieve nodes from the stack.

The detail of the implementation is in sourcecode. The time complexity and auxiliary space are both O(n) where n is the number of nodes of the tree.

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Stack](https://leetcode.com/tag/stack/) , [Tree](https://leetcode.com/tag/tree/) 

## Similar Questions

[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/), [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/), [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/), [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/), [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/), [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/), [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/), [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/), [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)
