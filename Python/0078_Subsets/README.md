# [78. Subsets](https://leetcode.com/problems/subsets)

## Description

Given a set of **distinct** integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## Solution

Let's take a look at the reorgnaized output of the example:

```
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

Initially we have [] in the list. Starting with considering 1, we add [1] into list. And then we consider 2 by appending 2 to [] and [1] to generate two new element [2] and [1, 2]. Now we have [], [1], [2], and [1,2] in our list. After all, we bring 3 in and we can get the result as above. 

We start the algorithm with one empty set element in the list. And we know in total the amount of subsets of number n is 2<sup>n</sup>, so we need 2<sup>n</sup>-1 operations to generate total amount of subsets. The time complexity is O(2<sup>n</sup>).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Backtracking](https://leetcode.com/tag/backtracking/) , [Bit Manipulation](https://leetcode.com/tag/bit-manipulation/) 

## Similar Questions

[Subsets II](https://leetcode.com/problems/subsets-ii/), [Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/), [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)
