# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)

## Description

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

Example 2:

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

## Solution

We use binary search twice. At the first time we find the begining from the whole array. And the we search for the end form the array started at the begining index we found at the first binary search to the end of the array. 

We run the binary search twice so that the time complexity is O(2logN) = O(2logN).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Binary Search](https://leetcode.com/tag/binary-search/) 

## Similar Questions

[First Bad Version](https://leetcode.com/problems/first-bad-version/)
