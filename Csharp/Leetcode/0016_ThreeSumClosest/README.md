# [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest)

## Description

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

## Solution

The logic is almost the same as [3Sum](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0015_ThreeSum). The differences are we don't neetd to find out all combinations and we find the closest sum to the target.

So we compare every combination to the target and record the minimum diff. After we examine all combinations, we get the result.

The length of the subarray we need to check starts from (n - 1) and all the way down to 1. Hence the total execution times is a arithmetic sequence and the order is O(n^2).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 

## Similar Questions

[3Sum](https://leetcode.com/problems/3sum/), [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/)
