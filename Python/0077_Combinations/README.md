# [77. Combinations](https://leetcode.com/problems/combinations)

## Description

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

## Solution

Implement a typical backtracking algorithm by recursion. The total amount of combinations is C(n, k) which is n!/(n-k)!k!. Hence the time coplexity is O(n!). The space of function stack we need is O(k).

## Related Topics

[Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Combination Sum](https://leetcode.com/problems/combination-sum/), [Permutations](https://leetcode.com/problems/permutations/)
