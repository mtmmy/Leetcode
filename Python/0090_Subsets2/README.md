# [90. Subsets II](https://leetcode.com/problems/subsets-ii)

## Description

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

## Solution

We use the same algorithm as in [78. Subsets](https://github.com/mtmmy/Leetcode/tree/master/Python/0078_Subsets) with a slightly change in order to elimlate duplicates.

```
1. [[], [1]]
2. [[], [1], [2], [1, 2]]
3. [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
```
Here we can see the result when each iteration finished. At the second iteration, we have a number, 2, which is different from the previous number, 1. Under this condition, we keep the current result size which is only 2. The purpose of this checking is that we've used **2** to generate new subsets. If the next number is also **2**, we can start at the subsets that havn't been append with **2**. Hence we can prevent creating duplicate subsets.

The time complexity and auxiliary space are O(2<sup>n</sup>).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Subsets](https://leetcode.com/problems/subsets/)
