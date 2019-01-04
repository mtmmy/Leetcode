# [112. Path Sum](https://leetcode.com/problems/path-sum)

## Description

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

## Solution

We use DFS to traverse each path. For every recursive call, we have the sum from the root to the current node. If the node is a leaf and the sum is equal to the target, we find the path and return true. Otherwise we keep searching.

The time complexity is O(n) and space complexity is O(log n) which is the height of the tree.

## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) 

## Similar Questions

[Path Sum II](https://leetcode.com/problems/path-sum-ii/), [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/), [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/), [Path Sum III](https://leetcode.com/problems/path-sum-iii/), [Path Sum IV](https://leetcode.com/problems/path-sum-iv/)
