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

We maintain a matrix **dp** where **dp[i][j]** indicates whether **s[i:j]** is a palindrome or not.

First we set **dp[i][i]** for each i to true because a single character is no doubt palindromic.

Later we check the length of 2. If two consective characters are the same, the string of two characters is a palindrome.

Finally, we need to check the length of greater than 2. In this section, we need to get the ending index, **j**, which is the starting index, **i**, plus the length. A substring is palindromic if characters of these two indices are the same, and its substring which is **s[i+1:j-1]** is also palindromic. Among all palindromic substrings, we find the longest one and return it.

The time complexity and auxiliary space are both O(N<sup>2</sup>).

## Related Topics

[String](https://leetcode.com/tag/string/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/), [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/), [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/), [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/), [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
