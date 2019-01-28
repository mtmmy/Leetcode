# [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)

## Description

Implement a trie with insert, search, and startsWith methods.

Example:

```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```

Note:

- You may assume that all inputs are consist of lowercase letters a-z.
- All inputs are guaranteed to be non-empty strings.

## Solution

We only build a path when a word is inserted. Example:

```
trie.insert("apple");

root
  \
   a
    \
     p
      \
       p
        \
         l
          \
           e
            \
             1
             

trie.insert("app"); 

root
  \
   a
    \
     p
      \
       p
      / \
     1   l
          \
           e
            \
             1
```

And we also use a extra 1 at the leaf node to mark it's a word which can help us to implement search. In the **search()**, we know it's not in the trie if we can find that word or we find the word and children of the last letter doesn't include **1**. For the **startWith()**, we do the same thing as for the **search()** without checking **1**.

## Related Topics

[Design](https://leetcode.com/tag/design/) , [Trie](https://leetcode.com/tag/trie/) 

## Similar Questions

[Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/), [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/), [Replace Words](https://leetcode.com/problems/replace-words/), [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)
