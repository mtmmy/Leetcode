# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

```
Input: ["flower","flow","flight"]
Output: "fl"
```

Example 2:

```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

Note:

All given inputs are in lowercase letters a-z.

## Solution
Just compare every strings to the first string in the list character by character. Once we found a string which is shorter than the current index or has a different characters, we stop comparing and the the substring from the begining to the current index of the first string in the list is the longest common prefix. If we go through whole characters of the first string in the list, the first string is the longest common prefix.

We only compare each character not in the first stirng once. Hence the time complexity is linear.

## Related Topics

[String](https://leetcode.com/tag/string/) 
