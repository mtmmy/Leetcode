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

We use the divide and conquer approach. We divide the problem into two parts first, left and right. Left part and right part are simple. We just find the maximum summation of a subarray from both of them. However, we can't only consider two parts, there may be a case the maximum subarray lies across two sides.

In the middle part, we also seperate it into left and right. We find the maximum summation from both sides. We get the maximum as follows because there may be negative numbers:

```
Math.Max(rightMax + leftMax, Math.Max(rightMax, leftMax))
```
The basic operations of this solution can be shown as follow:

```
T(n) = 2T(n/2) + n
```
After calculating we get:

```
n + nlogn
```
which is O(nlogn).