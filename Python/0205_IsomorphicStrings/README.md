# [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings)

## Description

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

```
Input: s = "egg", t = "add"
Output: true
```

Example 2:

```
Input: s = "foo", t = "bar"
Output: false
```

Example 3:

```
Input: s = "paper", t = "title"
Output: true
```

Note:
You may assume both s and t have the same length.

## Solution

We use two hash tables to track the position of the last appearance of each character of each string. If at any moment that the position of two strings are different, strings are not isomorphic.

Time complexity: O(n)<br>
Space complexity: O(1)

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) 

## Similar Questions

[Word Pattern](https://leetcode.com/problems/word-pattern/)
