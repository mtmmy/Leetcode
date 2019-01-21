# [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)

## Description

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Example:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

## Solution

We use two pointers start from head and tail of the array. If the sum of two numbers that two pointers point to equals to the target number, it's the result. When the sum is smaller than the target, we move the head pointer one step to right; when the sum is greater than the target, we move the tail pointer one step to left. If there are no mathced result, the loop will end when two points meet.

Time complexity: O(n)<br>
Space complexity: O(1)

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) , [Binary Search](https://leetcode.com/tag/binary-search/) 

## Similar Questions

[Two Sum](https://leetcode.com/problems/two-sum/), [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
