# [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)

## Description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

```
Input: [3,4,5,1,2] 
Output: 1
```

Example 2:

```
Input: [4,5,6,7,0,1,2]
Output: 0
```

## Solution

First we check if the last number is greater than the first number, it means the array has not been rotated and we just return the first number.

Otherwise, We use binary search method to solve this problem. We set the condition of the loop as left < right - 1, which helps us find the boundry of the largest number and the min number and we just return the number that the right pointer points.

Time complexity: O(n log n)<br>Space complexity: O(1)

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Binary Search](https://leetcode.com/tag/binary-search/) 

## Similar Questions

[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/), [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
