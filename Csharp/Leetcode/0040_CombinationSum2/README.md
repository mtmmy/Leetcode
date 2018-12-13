# [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii)

## Description

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

Example 1:

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

Example 2:

```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

## Solution

This question is similar to [39. Combination Sum](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0039_CombinationSum). The differences are candidates may be duplicates and each candidates can only be used once. Hence we can use the same algorithm as of [39. Combination Sum](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0039_CombinationSum) and eliminate duplicates.

The time complexity and space complexity will be the same with [39. Combination Sum](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0039_CombinationSum).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Combination Sum](https://leetcode.com/problems/combination-sum/)
