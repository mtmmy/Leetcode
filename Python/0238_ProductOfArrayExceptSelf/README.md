# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)

## Description

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## Solution

The first loop will get the product of all elements on the left. For example:

```
input: [1,2,3,4]
result: [1, 1, 2, 6]
```

The second loop will generate the porduct on the right side.

```
inputs: [1,2,3,4]
prodR: [24,12,4,1]
```

and we multiply it back to the result at the corresponding position and we get the correct answer.

Time complexity: O(n)<br>
Space complexity: O(n)

## Related Topics

[Array](https://leetcode.com/tag/array/) 

## Similar Questions

[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/), [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/), [Paint House II](https://leetcode.com/problems/paint-house-ii/)
