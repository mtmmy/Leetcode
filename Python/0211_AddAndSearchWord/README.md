# [211. Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design)

## Description

Design a data structure that supports the following two operations:

```
void addWord(word)
bool search(word)
```

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```

Note:
You may assume that all words are consist of lowercase letters a-z.

## Solution

We set up a hash table with length of words as keys and the corresponding values is a list to store words with such length. For searching, we detect if the input contains any dot first. If it doesn't, we simply search for the word or we need to take care dots in the searching.

Time complexity: <br>
addWord(): O(1)<br>
search(): O(n) for words without dots; O(n * l) for words with dots where l is the length of the word

## Related Topics

[Backtracking](https://leetcode.com/tag/backtracking/) , [Design](https://leetcode.com/tag/design/) , [Trie](https://leetcode.com/tag/trie/) 

## Similar Questions

[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/), [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)
