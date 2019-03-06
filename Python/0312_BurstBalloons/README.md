# [312. Burst Balloons](https://leetcode.com/problems/burst-balloons)

## Description

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

- You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

```
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

## Solution

For covinient, we add two 1s at the head and tail of the original array. And we create a two-dimension array called **dp**. Where **dp[i][j]** denotes the maximum coins we can earn by bursting balloon i to balloon j in some order.

And then we set up a recursive function with two parameters: **left** and **right** which represent the positions of the left most ballloon and the rightmost balloon. 

```
n = len(nums)
nums.insert(0, 1)
nums.append(1)
dp = [[0] * len(nums) for _ in range(len(nums))]

def burst(left, right):
    if left > right:
        return 0
    if dp[left][right] > 0:
        return dp[left][right]
    result = 0
    for k in range(left, right + 1):
        result = max(result, nums[left - 1] * nums[k] * nums[right + 1] + burst(left, k - 1) + burst(k + 1, right))
    dp[left][right] = result
    return result
return burst(1, n)
```

The first two conditions are easy to understand. The last part is to find in the range between **left** and **right**, which balloon **k** could lead to the maximum coins.

Time complexity: O(N<sup>3</sup>)<br>
Space Complexity: O(N<sup>2</sup>)

## Related Topics

[Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 