# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)

## Description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

Example 2:

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## Solution

We use binary search to solve this. Since the array has been rotated, we need more check than original binary search. We check nums[end] and nums[mid] first, if nums[end] is smaller or equal to snums[mid], it means the right part isn't sorted, so we check if target is in the left part. If it is, we go to the left part, otherwise we go to the right part. if nums[end] is greater than snums[mid], the right part is sorted. Then we check where the target is and go to that part. In the end, we will find a nums[mid] equals to the target, if we don't, the target is not in the array. 

We need twice comparisons than the original binary search. Hence the time complexity is O(2logN) = O(logN).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Binary Search](https://leetcode.com/tag/binary-search/) 

## Similar Questions

[Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/), [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
