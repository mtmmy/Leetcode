# [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum)

## Description

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

Example 2:

```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

## Solution

We use an external variable to keep the maximum sum and recursively find each path sum. The details of implementation are:

1. Find the path sum of left subtree. In case the result is negative, we find the maximum value between the zero and the path sum.
2. Find the path sum of right subtree. In case the result is negative, we find the maximum value between the zero and the path sum.
3. Store the maximum value between the maximum path sum so far and the current one which is the sum of path sum of the left subtree, that of the right subtree, and the value of the current node.
4. Return the value of the current node plus the bigger one of the path sum of the left subtree and that of the right subtree.

Since we use the DFS to traverse the tree just once, the time complexity is O(n) and the space complexity is O(log n).

## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) 

## Similar Questions

[Path Sum](https://leetcode.com/problems/path-sum/), [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/), [Path Sum IV](https://leetcode.com/problems/path-sum-iv/), [Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)
