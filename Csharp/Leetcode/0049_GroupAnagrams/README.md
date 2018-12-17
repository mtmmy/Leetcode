# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams)

## Description

Given an array of strings, group anagrams together.

Example:

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

Note:

- All inputs will be in lowercase.
- The order of your output does not matter.

## Solution

Anagrams are a words, phrases, or names formed by rearranging the letters of another, such as *cinema*, formed from *iceman*. In order to group anagrams, we need to know their composition first. The key of each word will be the alphabetical rearranging the letters it consist of. For example, the key of *cinema* and *iceman* is *aceimn*. The straitforward solution for rearrangin is sorting. However, we don't really need to use sorting algorithm. We can rearrange a word by counting the apperarance of each letter which can reduce execution time.

After recieving keys, we can easily group words by using hash table. The time complexity is O(m\*n) where m is the number of words and n is the average length of words. And the space complexity is O(n). 

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [String](https://leetcode.com/tag/string/) 

## Similar Questions

[Valid Anagram](https://leetcode.com/problems/valid-anagram/), [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/)
