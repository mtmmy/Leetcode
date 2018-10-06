# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

## Description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Note that an empty string is also considered valid.

Example 1:

```
Input: "()"
Output: true
```

Example 2:

```
Input: "()[]{}"
Output: true
```

Example 3:

```
Input: "(]"
Output: false
```

Example 4:

```
Input: "([)]"
Output: false
```

Example 5:

```
Input: "{[]}"
Output: true
```

## Solution

We can use stack to solve this problem. When we read left parentheses, we just push it into the stack. If we read right parentheses, we need to check if it's valid. If we can't find the corresponding left parentheses at the top of the stack, then it's not valid. Otherwise, it's valid and we keep reading new parentheses.