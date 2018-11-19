# [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words)

## Description

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

```
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
```

Example 2:

```
Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
```

## Solution

We use two hash tables, one stores counts of each words in **words**, the other stores counts of words when we are examining **s**. First we run through **words** and store counts of each word in **countTable1**. Later we check **s**, for each character, we use a nested loop to count the number of each words. If the word doesn't in the **countTable1** or the number of the word in the **countTable2** is more than that of in **countTable1**, it means the substring is not built by **words**, we move on to the next charcter. Otherwise we store the starting index. 

Let's say length of **s** is m and total characters in **words** is n. The worst case time complexity will be O(m*n) which means for every charcter in **s**, we need to check for every words in **words**.

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) , [String](https://leetcode.com/tag/string/) 

## Similar Questions

[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
