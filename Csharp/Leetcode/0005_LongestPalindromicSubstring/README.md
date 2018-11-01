# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)

## Description

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

Example 2:

```
Input: "cbbd"
Output: "bb"
```

## Solution

First we insert "." into every two characters. After doing this, we get a string like "c.b.b.d" which allows us only considering odd length cases. And we find the palindromic length for each character as the pivot. Afterward we get the longest palindromic string and its pivot so we can return the substring. The time complexity of the solution is O(n^2) since for each character we may need to check n/2 characters.

## Related Topics

[String](https://leetcode.com/tag/string/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/), [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/), [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/), [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/), [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
