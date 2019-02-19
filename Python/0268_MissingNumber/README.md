# [268. Missing Number](https://leetcode.com/problems/missing-number)

## Description

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

```
Input: [3,0,1]
Output: 2
```

Example 2:

```
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

## Solution

Solution 1:

Since we know the numbers will in the 0 ~ n range and there will only miss one number. Then we can sum up 0 ~ n and minus **sum(nums)** and the answer is the missing number.

Time complexity: O(n)<br>
Space complexity: O(1)

Solution 2:

We can use XOR to solve this problem as well becasue we know we get zero when we XOR two same numbers. The range of the number is 0 ~ n, and if there is no missing number, the answer is n. Thus we set our defaut value of result as n because if there is know missing number and we execute the following loop, n will be the remaining number. If the number is between 0 ~ n-1, n will be eliminate by **result ^ nums[i]** somewhere in the loop and the missing number is the only one number that appears once in the XOR process.

```
for i in range(len(nums)):
    result = result ^ i ^ nums[i]
```

Time complexity: O(n)<br>
Space complexity: O(1)

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Math](https://leetcode.com/tag/math/) , [Bit Manipulation](https://leetcode.com/tag/bit-manipulation/) 

## Similar Questions

[First Missing Positive](https://leetcode.com/problems/first-missing-positive/), [Single Number](https://leetcode.com/problems/single-number/), [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/), [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/)
