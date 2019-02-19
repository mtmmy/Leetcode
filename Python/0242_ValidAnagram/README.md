# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram)

## Description

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

```
Input: s = "anagram", t = "nagaram"
Output: true
```

Example 2:

```
Input: s = "rat", t = "car"
Output: false
```

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

## Solution

Solution 1:

Sort two string and compare them.<br>
Time complexity: O(n log n)<br>
Space complexity: O(1)

Solution 2:

Use a hash table to store how many times a character show in string **s**. And minus the number of that character that appear in the string **t**. At the end we check the value in the hash table, if there exist any chararcter whose value is not zero, two string are not valid anagram.

Time complexity: O(n)<br>
Space complexity: O(n)

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Sort](https://leetcode.com/tag/sort/) 

## Similar Questions

[Group Anagrams](https://leetcode.com/problems/group-anagrams/), [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/), [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
