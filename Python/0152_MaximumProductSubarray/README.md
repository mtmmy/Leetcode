# [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray)

## Description

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

Example 2:

```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

## Solution

We keep multiplying numbers from the begining of the array. Meanwhile, we need to maintain the biggest and the smallest product so far. The reason that we need not only the biggest but also the smallest is that when the smallest is negative and the next number is also negative, the product will become positive and it may be the biggest.

Time complexity: O(n)<br>Space complexity: O(1)

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/), [House Robber](https://leetcode.com/problems/house-robber/), [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/), [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/), [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
