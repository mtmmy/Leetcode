# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses)

## Description

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

```
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
```

Example 2:

```
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

## Solution

We use a array **dp** to implement dynaic programming with definition that **dp[i]** is the longest valid parentheses of **s[0, i-1]** and that parentheses contains **s[i-1]**. The variable **j** indicates the charcters before the longest valid parentheses of **dp[i-1]**. We also need a varaible **longest** to keep the size of the longest valid parentheses. 

We have two situations, valid and invalid. When **s[i-1]** is "(", it's ceritanly not valid because the parentheses can't end with "("; when **j < 0**, it means the string it's not long enough to attain a valid parentheses; when **s[j]** is ")", it's not valid because a valid parentheses can't start with ")". In these situations, we all set **dp[i]** as 0. Otherwise, we have valid parenthese and we want to know the length of it. The length of it will be **(LVP at dp[i-1]) + 2 + (LVP at dp[j])** where the first part is the LVP between s[j+1, i-1], the 2 is the valid pair at s[j] and s[i-1], and the third part is the LVP ends at s[j-1]. 

The time complexity is O(n) and space complexity is O(n) as well. 

## Related Topics

[String](https://leetcode.com/tag/string/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
