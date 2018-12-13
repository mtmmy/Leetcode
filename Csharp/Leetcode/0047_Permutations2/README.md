# [47. Permutations II](https://leetcode.com/problems/permutations-ii)

## Description

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

## Solution

This problem is similar to the problem [46. Permutations](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0046_Permutations). The difference is that there may be duplicates in this problem. However, the method we used in [46. Permutations](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0046_Permutations) cannot record wheather the value is used or not so we cannot skip duplicate permutations.

So we use a similar solution of problem [39. Combination Sum](https://github.com/mtmmy/Leetcode/tree/master/Csharp/Leetcode/0039_CombinationSum). We use a list to store each result and when the length of the list equals to the amount of input numbers, we store the list to the result. And we skip elements when 1. It has been used or 2. The value is same as the previous one and the previous one has not been used yet. By doing these, we can avoid duplicate permutations.

Since the number of permutaions of N numbers is N!, the time complexity of finding all permutations is O(N!).

## Related Topics

[Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Next Permutation](https://leetcode.com/problems/next-permutation/), [Permutations](https://leetcode.com/problems/permutations/), [Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/)
