# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray)

## Description

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Solution

Simple dp solution. We use a variable to keep the maximum summation we can get at the current index. To get this value, we compare the number itself and the sum of previos max and the number. And we use another variable to keep global maximum value. Once we finished iteration, we get the maximum sum.

[Follow up solution is here](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0053_MaximumSubarray)