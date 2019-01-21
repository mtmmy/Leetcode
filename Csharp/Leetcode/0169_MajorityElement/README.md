# [169. Majority Element](https://leetcode.com/problems/majority-element)

## Description

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

```
Input: [3,2,3]
Output: 3
```

Example 2:

```
Input: [2,2,1,1,1,2,2]
Output: 2
```

## Solution

Go through the array once and use an extra space (space complexity is O(n)) to store the number of each numbers so that the time complexity is O(n).

The other solution is [Moore voting algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) which takes O(n) time and constant space.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/) , [Bit Manipulation](https://leetcode.com/tag/bit-manipulation/) 

## Similar Questions

[Majority Element II](https://leetcode.com/problems/majority-element-ii/)
