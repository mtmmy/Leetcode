# [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings)

## Description

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:

```
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
```



Example 2:

```
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
```



Note:



## Solution



## Related Topics

[Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Edit Distance](https://leetcode.com/problems/edit-distance/), [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/), [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)
