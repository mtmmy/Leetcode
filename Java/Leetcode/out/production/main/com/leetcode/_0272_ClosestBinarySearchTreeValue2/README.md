# [272. Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii)

## Description

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

- Given target value is a floating point.
- You may assume k is always valid, that is: k ≤ total nodes.
- You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example:

```
Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
```

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

## Solution

We inorder traverse the BST and use a queue to store the result. If the size of the queue is less than **k**, we simply push the node to queue. If the size of the queue is already **k**, we compare the difference of the target and the current node with that of the head node in the queue. If the difference of the current node is smaller, we pop the head from the queue and push the current node into the queue.

The reason that we can use a queue and only compare the head is because inorder traversing of a BST is reading nodes in ascending order. There are three situations. The first one is target is smaller than all nodes, then the first node we put in the queue will be the one with the smallest difference and all other nodes will compare to it after the queue is full and be ignore. The second one is the target is greater than all ndoes, then we will keep pop nodes from the queue and push new node in it. The third is the target lies within all nodes. In this situation, the difference will get samller with traversing at the beging and the queue keeps k nearest nodes until the value of node surpass the target along with the increasing of the difference. At the surpassing moment, the head of the queue is the k-th nearest so we can only compare to it.

Time complexity: O(n)
Space complexity: max(O(k), O(log n))

## Related Topics

[Stack](https://leetcode.com/tag/stack/) , [Tree](https://leetcode.com/tag/tree/) 

## Similar Questions

[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/), [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/)
