# [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator)

## Description

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
![](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)

```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
```

Note:

- next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
- You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

## Solution

We maintain a stack who stores from root to the leaf of farest left side of the tree from the bottom to top. When the hasNext is called, we can know the answer by checking if the stack is empty. When next() is called, we first pop out the top node in the stack and push the left arm of its right sub tree if it has one. And we just return the value of the top node.

We use the example above to illustrate. We represent the state of the stack after every function call.

```
BSTIterator iterator = new BSTIterator(root);
stack: [7, 3]
iterator.next();    // return 3
stack: [7]
iterator.next();    // return 7
stack: [15, 9]
iterator.hasNext(); // return true
iterator.next();    // return 9
stack: [15]
iterator.hasNext(); // return true
iterator.next();    // return 15
stack: [20]
iterator.hasNext(); // return true
iterator.next();    // return 20
stack: []
iterator.hasNext(); // return false
```

## Related Topics

[Stack](https://leetcode.com/tag/stack/) , [Tree](https://leetcode.com/tag/tree/) , [Design](https://leetcode.com/tag/design/) 

## Similar Questions

[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/), [Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/), [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/), [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/), [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)
