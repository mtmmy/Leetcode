# [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii)

## Description

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```



return its bottom-up level order traversal as:

```
[
  [15,7],
  [9,20],
  [3]
]
```



## Solution

We use DFS. First we put the root node into a queue and create a loop which runs until the queue is empty. Inside the loop we have another loop that runs same amount of times of the length of queue. And we need to keep this value becaase in the loop we will add nodes into the queue. For example, at the beginning there is only the root node in the queue, this inner loop is executed once. In the inner loop, we dequeue each node and store the value of the node to a temporary list and add its child into the queue. After the execution of the inner loop, we add the temporary list to the result list. If there are no nodes in the queue, the programm ends and returns the reversed result list. Otherwise the programm keeps running.

The time complexity and space complexity are both O(n).

## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) 

## Similar Questions

[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/), [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)
