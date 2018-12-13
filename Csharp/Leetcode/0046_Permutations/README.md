# [46. Permutations](https://leetcode.com/problems/permutations)

## Description

Given a collection of distinct integers, return all possible permutations.

Example:

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## Solution

Combination and Permutation, for these kinds of problems, we generally use recursion to solve them. For this problem, we use a recursive function. For looking for all permutations of N elements, we alredy have all permutations of (N-1) elements, so we just insert N-th element to every index of all permutations of (N-1) elements.    
    
For example, we are looking for permutations of [1, 2, 3], so we already have permuations of [2, 3] which are [2, 3] and [3, 2]. And we insert 1 into gaps of each array. For [2, 3], after insertion, we get [1, 2, 3], [2, 1, 3] and [2, 3, 1]. For [3, 2], after insertion, we get [1, 3, 2], [3, 1, 2] and [3, 2, 1].

Since the number of permutaions of N numbers is N!, the time complexity of finding all permutations is O(N!).

## Related Topics

[Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Next Permutation](https://leetcode.com/problems/next-permutation/), [Permutations II](https://leetcode.com/problems/permutations-ii/), [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/), [Combinations](https://leetcode.com/problems/combinations/)
