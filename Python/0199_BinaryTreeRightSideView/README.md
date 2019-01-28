# [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)

## Description

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

## Solution

We use recursion to implement BFS and for each layer we store the rightmost to the result list. Since we need a temperary space for each layer and the maximum size of the layer is leaves of a complete tree so the space we need is still O(n).

Time complexity: O(n)<br>
Space complexity: O(n)

## Related Topics

[Tree](https://leetcode.com/tag/tree/) , [Depth-first Search](https://leetcode.com/tag/depth-first-search/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) 

## Similar Questions

[Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/), [Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/)
