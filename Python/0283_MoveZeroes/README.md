# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes)

## Description

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

Note:

1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.

## Solution

What we do in the first loop is that we write non-zero elements one by one from the head. After we inspect every non-zero elements, we fill up the remaining space with zeroes.

Time complexity: O(n)<br>
Space complexity: O(1)

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 

## Similar Questions

[Remove Element](https://leetcode.com/problems/remove-element/)
