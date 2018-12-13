# [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching)

## Description

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
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
p = "*"
Output: true
Explanation: '*' matches any sequence.
```

Example 3:

```
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

Example 4:

```
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
```

Example 5:

```
Input:
s = "acdcb"
p = "a*c?b"
Output: false
```

## Solution

We have two approaches to solve this problem. 

The first one is dynamic programming. We create a 2-D array so that dp[i][j] denotes whether s[i-1] matches p[j-1]. And the following code shows three situations we need to consider:

```
if p[i - 1] == "?":
    dp[i][j] = dp[i - 1][j - 1]
elif p[i - 1] == "*":
    dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
else:
    dp[i][j] = dp[i - 1][j - 1] and s[j - 1] == p[i - 1]  
```
After comparing two strings, we can learn whether two strings match or net by check the last element in the dp array. This algorithm takes O(m\*n) time and O(m\*n) space where m is the length of **s** and n is the length of **p**.

Another algorithm also uses dynamic programming.

1. Let **i** be the pointer of string **s**. Let **j** be the pointer of string **p**. Let **s_star** be the pointer of string **s** when we encounter "\*" in **p**. Let **p_star** be the pointer of string **p** when we encounter "\*".
2. When s[i] == p[j] or p[j] == ?, we increment both **i** and **j**.
3. When we meet "\*" in **p**, we keep the indices for both **s** and **p** by **s_star** and **p_star**. And we increment **j** to compare the next character of **p** with the current character of **s**.
4. If s[i] == p[j], it means we end up using "\*" to match a sequence (may be an empty sequence). Otherwise, we have to use "\*" to match some characters. So we increament **s_star** since the current character in **s** has been matched and increment **i = s_star** and **j = p_star + 1**. We stick **j** at the next charactor of "\*" so that we can check when we finish matching a sequence by using "\*".
5. If step 2 ~ 4 are invalid, it means **s[i] != p[j]** and we don't meet any "\*" so that **s** doesn't match **p**.
6. Last we check if **j** reaches the end of **p**.

This algorithm only takes O(n) time and constant space.


## Related Topics

[String](https://leetcode.com/tag/string/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) , [Backtracking](https://leetcode.com/tag/backtracking/) , [Greedy](https://leetcode.com/tag/greedy/) 

## Similar Questions

[Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
