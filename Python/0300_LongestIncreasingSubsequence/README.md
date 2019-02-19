# [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)

## Description

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

```
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```

Note:

- There may be more than one LIS combination, it is only necessary for you to return the length.
- Your algorithm should run in O(n<sup>2</sup>) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

## Solution

Solution 1:

```
n = len(nums)
if n <= 1:
    return n
dp = [1] * n
result = 0
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    result = max(result, dp[i])

return result
```    
We use an array to keep LIS where dp[i] denotes the LIS for the nums[0:i]. We set up a nested loop to compare the value of numbers. When the current number is larger than a previous number, we store max(dp[i], dp[j] + 1). And use a variable to store the global maximum LIS.

Time complexity: O(n<sup>2</sup>)<br>
Space complexity: O(n)

Solution 2:

```
dp = []
for i in range(len(nums)):
    left, right = 0, len(dp)
    while left < right:
        mid = left + (right - left) // 2
        if dp[mid] < nums[i]:
            left = mid + 1
        else:
            right = mid
    if right >= len(dp):
        dp.append(nums[i])
    else:
        dp[right] = nums[i]
return len(dp)
```

We use an array called **LIS** to store elements of LIS. For every number in **nums**, we use the binary search to find where can we put that number into and don't ruin the LIS. At last we will get a LIS and we simply return its length.

Time complexity: O(n log m) where n is the amount of numbers and m is the length of LIS.<br>
Space complexity: O(m)


## Related Topics

[Binary Search](https://leetcode.com/tag/binary-search/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/), [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/), [Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/), [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/), [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
