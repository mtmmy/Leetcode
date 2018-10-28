# [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching)

## Description

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```

The matching should cover the entire input string (not partial).

Note:

Example 1:

```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

Example 2:

```
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

Example 3:

```
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

Example 4:

```
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
```

Example 5:

```
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```

## Solution

To solve this problem, we can use dynamic programming. First of all, we allocate a two dimensional array of boolean where dp[i][j] denotes s[:i-1] matches p[:j-1]. Since the empty string matches the empty string, so dp[0][0] must be True and we can start from this. We use nested loop to go through dp array and check if string matches at the corresponding indices. First step, we ignore special characters "*" and ".", and only focus on the letters:

```
dp[i][j] = i > 0 and s[i - 1] == p[j - 1] and dp[i - 1][j - 1]
```
which means if s[i-1] and p[j-1] are the same character and s[:i-2] matches p[:j-2], s[:i-1] matches p[:j-1].

Next, we need to consider special characters. We first check ".", which matches any single characters so that we can only check if s[:i-2] matches p[:j-2] or not:

```
dp[i][j] = i > 0 and dp[i - 1][j - 1]
```

After that, we look at *, which means zero or more of the character before the *.

```
dp[i][j] = (dp[i][j - 2]) or 
	(i > 0 and dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == "."))
```
We have to check two parts. First, does s[:i-1] matches p[:j-3]? This check means we consider .* as zero characters. Second, we check if s[:i-2] matches p[:j-1] which means does s[:i-2] matches the p before the * and check the charcter before the * matches.

After all, the element at the last columne of the last row is our answer because it means if s matches p or not. Total amount of checking operations of this solution is (m + 1)(n + 1) = mn + m + n + 1. Hence the time complexity is O(mn) and the space complexity is also O(mn).