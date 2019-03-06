# [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self)

## Description

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

```
Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

## Solution

Binary Search Tree:

```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None
                    
class Solution:
    def add(self, root, val):
        curCount = 0
        while 1:
            if val <= root.val:
                root.count += 1
                if not root.left:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
            else:
                curCount += root.count
                if not root.right:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
        return curCount
    
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        if not nums:
            return []
        
        root = TreeNode(nums.pop())
        result = [0]
        for val in reversed(nums):
            result.append(self.add(root, val))
            
        return result[::-1]
```

First we need to setup a tree class with one extra paramter **count** who counts smaller numbers on its left and starts from 1. The reason that the paramter starts from one is that the node who will access this parameter must be greater than the current node.

Second we use the last number in the array as the root to build a tree. And then we retrive the array in the reversed order. For each number, we compare it to nodes in the tree starting from the root. If the number is smaller or equal to the value of the current node, we increment node.count. And we generate a new node as the left child of the current node if the current node doesn't have a left child, otherwise we set its left child to the current node and continue the loop. If the number is greater than the value of the current node, we add up node.count to the temp variable. Because the node.count denotes how many smaller numbers at the left-hand side of the current node and these nodes including the current node are at the right-hand side of the current number. After than, we setup a node if the current node has no right child, otherwise we use the right child as the current node and continue the loop.

After the loop is finished, the **curCount** is numbers that is smaller and on the right hand side of the current number. And the tree will become a binary search tree.

The worst case happens when the number is sorted (ascendingly or descendingly). In this scenario, the tree will become one-side. The time complexity is O(n<sup>2</sup>). Generally when the tree is balanced, the time complexity is O(n log n).

Space complexity: O(n)

Merge Sort:

```
result = [0] * len(nums)
        
def sort(enum):
    half = len(enum) // 2
    if half:
        left, right = sort(enum[:half]), sort(enum[half:])
        for i in range(len(enum))[::-1]:
            if not right or left and left[-1][1] > right[-1][1]:
                result[left[-1][0]] += len(right)
                enum[i] = left.pop()
            else:
                enum[i] = right.pop()
    return enum
    
sort(list(enumerate(nums)))
return result
```

This solution is similar to the classic merge sort. The difference is we compare sub-arrays from the tail to the head. If the last element of the left sub-array is greater than the that of the right one, the whole right sub-array is smaller than that element. So we add this amount to the corresponding index. Details are shown in the code.

Time complexity: O(n log n)<br>
Space compelxity: O(n)

## Related Topics

[Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/) , [Binary Indexed Tree](https://leetcode.com/tag/binary-indexed-tree/) , [Segment Tree](https://leetcode.com/tag/segment-tree/) , [Binary Search Tree](https://leetcode.com/tag/binary-search-tree/) 

## Similar Questions

[Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/), [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/), [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)
