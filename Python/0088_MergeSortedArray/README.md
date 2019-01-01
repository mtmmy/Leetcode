# [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array)

## Description

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

- The number of elements initialized in nums1 and nums2 are m and n respectively.
- You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

## Solution

We start filling up numbers backward from the end of **nums1**. Since arrays are sorted, we keep picking up the bigger one and put it at **nums1**. If there are some numbers in **nums2** after the loop ends, we copy those to **nums1**.

The time complexity is O(N) and auxiliary space is O(1).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 

## Similar Questions

[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
