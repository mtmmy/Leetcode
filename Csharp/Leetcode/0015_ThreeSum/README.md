# [15. 3Sum](https://leetcode.com/problems/3sum)

## Description

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

## Solution

First, we can consider this as an extended problem from [Two Sum](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0001_TwoSum). The solution will be as following:  

1. Sort the list  
2. Pick a current number in ascending order  
3. Finding the two-sum result from numbers greater than the current number in the list with the target number of two-sum is the negative current number.  

Sorting helps us skipping duplicates easily and making searching for two-sum results easier. The time complexity is O(n^2) since the time complexity of two-sum in a sorted array is O(n) and we have a size of n list.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 

## Similar Questions

[Two Sum](https://leetcode.com/problems/two-sum/), [3Sum Closest](https://leetcode.com/problems/3sum-closest/), [4Sum](https://leetcode.com/problems/4sum/), [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/)
