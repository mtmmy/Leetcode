# [198. House Robber](https://leetcode.com/problems/house-robber)

## Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

Example 2:

```
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

## Solution

We use dynamic programming to solve this problem. We generate a list which has the same size of the input. In this list, **dp[i]** denotes the maximum money can be robbed at the i-th house. The way we get this value is, either we don't rob house i, the value is **dp[i - 1]**, or we rob house i and the money is **dp[i - 2] + nums[i]**, and we pick the larger one. The value of the last element of **dp** is the maximum money we can rob.

Time complexiy: O(n)<br>
Space complexity: O(n)

## Related Topics

[Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/), [House Robber II](https://leetcode.com/problems/house-robber-ii/), [Paint House](https://leetcode.com/problems/paint-house/), [Paint Fence](https://leetcode.com/problems/paint-fence/), [House Robber III](https://leetcode.com/problems/house-robber-iii/), [Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/), [Coin Path](https://leetcode.com/problems/coin-path/), [Delete and Earn](https://leetcode.com/problems/delete-and-earn/)
