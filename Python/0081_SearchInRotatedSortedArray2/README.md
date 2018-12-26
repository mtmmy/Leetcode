# [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)

## Description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

Example 2:

```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

Follow up:

- This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
- Would this affect the run-time complexity? How and why?

## Solution

This is an altered binary search problem. We still use two pointers, **left** and **right**. And in the loop with the condition **left <= right**, we calculate **mid** every iteration.

In the iteration, we need to decide which part we want to cut off. There are four situations shown in the source code. By keeping cutting off useless part, we can either find the target and return true or failing the condition of the loop and return false.

The time complexity of binary search is O(logN) and auxiliary space is O(1).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Binary Search](https://leetcode.com/tag/binary-search/) 

## Similar Questions

[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
