# [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list)

## Description

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

## Solution

We recursively flatten every subtree from the right part of the tree. The step by step process that the algorithm works on the given example is as follows:

1. 

```
    1
   / \
  2   5
 / \   \
3   4   6
```

The right part of the root node has already been flatten, so there's no change.

2.

```
    1
   / \
  2   5
   \   \
    3   6
     \
      4
```

We flatten the subtree which root node is 2.

3.

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```
We flatten the whole tree.

The time complexity is O(n) and the space complexity is O(log n) which is the height of the original tree.

## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) 

## Similar Questions

[Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)
