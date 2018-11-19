# [31. Next Permutation](https://leetcode.com/problems/next-permutation)

## Description

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

## Solution

First we find the last index where **nums[i]** > **nums[i - 1]**. If there are no such index, it means the array is stored in reversed way, we just reverse whole array. If there is a such index, it's the place we need to swap to get the next permutation. Then we find the last index where **nums[j]** > **nums[i - 1]** and swap values in j and i-1. And we need to reverse all numbers in nums[i:end] becasue they are all store in a reversed way. 

The time complexity is O(n) because we only iterate whole array twice at most. 

## Related Topics

[Array](https://leetcode.com/tag/array/) 

## Similar Questions

[Permutations](https://leetcode.com/problems/permutations/), [Permutations II](https://leetcode.com/problems/permutations-ii/), [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/), [Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/)
