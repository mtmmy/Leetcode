# [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning)

## Description

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

```
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```

## Solution

We first create a 2-d list called **isPal** using dynamic programming where **isPal[i][j]** indicates whether s[i:j] is a palindrome or not. After the list is built up, we use DFS to implement the backtracking strategy to find all possible  palindrome partitioning of s.

## Related Topics

[Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)
