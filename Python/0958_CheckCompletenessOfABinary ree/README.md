# [958. Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree)

## Description

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

![image](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png)

```
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
```

Example 2:

![image](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png)

```
Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
```

Note:

1. The tree will have between 1 and 100 nodes.

## Solution

We just use BFS to traverse the whole tree. Once we encounter a null element, we stop the BFS prcedure and check the queue. The reason in that the complete tree can only have vacant node at the leaf level. 

The way we check is to confirm that whether there are non-null nodes after the first found null element in the queue. Accroding the the definition of the complete tree, nodes have to be as far left as possibile.

The algorithm runs BFS once, so the time complexity is O(N). And the queue needs the same size of the number of nodes of the tree, so the space complexity is also O(N).

## Related Topics

[Tree](https://leetcode.com/tag/tree/) 
