# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree)

## Description

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

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

return its depth = 3.

## Solution

We can divide the problem into two problem. The maximum depth of the tree with the root node is:

```
max(depth(root.left), depth(root.right)) + 1
```

Hence we can use this divide and conquer method to build a recursive function. The detail is in the sourcecode.

The time complexity is O(n) and the space complexity is the height of the tree which is O(log n).

## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) 

## Similar Questions

[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/), [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/), [Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)
