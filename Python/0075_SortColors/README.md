# [75. Sort Colors](https://leetcode.com/problems/sort-colors)

## Description

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

Follow up:

## Solution

A simple solution is to use in-place sort algorithms such as quick sort. They take O(NlogN) time. However, we can solve this problem in just O(N).

We use two pointers called **red** and **blue** to denote the index of the last red and that of the first blue. The initial position of **red** is the begining point of the array and that of **blue** is the end point of the array. The algorithm is:

1. set a index **i** starting from 0
2. if nums[i] == 0 (it's red), swap nums[i] and nums[red]; increase red by 1
3. if nums[i] == 2 (it's blue). swap nums[i] and nums[blue]; decrease blue and i both by 1

The time complexity of this algorithm is O(N).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) , [Sort](https://leetcode.com/tag/sort/) 

## Similar Questions

[Sort List](https://leetcode.com/problems/sort-list/), [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/), [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)
