# [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree)

## Description

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

- a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

```
    3
   / \
  9  20
    /  \
   15   7
```

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```

Return false.

## Solution

The idea of this solution is that we go through the tree with DFS. When we reach the leaf nodes, they will return 1 which means the depth that count from themself to the bottom of the tree is 1.

Every node will get the depth from its children. We compare the depth of children of the node. If the differnce of two children is greater than 1, we return -1 to leave the recursive function. At the end of the program we only need to check if result equals to -1 or not.

The time complexity is O(n) since we use DFS to traverse the tree once. The space complexity is O(log n) which is the maximum size of the function stack and is also the height of the tree.

## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) 

## Similar Questions

[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
