# [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii)

## Description

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

1. Only one letter can be changed at a time
2. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

- Return an empty list if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
```

Example 2:

```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```

## Solution

The basic idea of this algorithm is that we start from the beginWord and create all possible words that coverted from the beginWord with one character different and check among these words which are in the wordList to form the next layer of words. (We eliminate used words from wordList so there will be no cycle formed.) After the next layer has been generated, we use this layer as the role like the beginWord to generate the next layer. 

However, if we just follow this procedure, the algorithm will end up with all possible ladders not just only the shortest one. So here we introduce a trick which if we build up the ladder from the both side, front and back. The front side starts with beginWord and the back side starts with endWord. And we choose the one contains fewer words of front side and back side to operate the algorithm. Once these two side contain one or more overlaped word, the ladders formted by those words are guaranteed to be the shortest ladders.

To figure out the time complexity of this algortihm, we can split it into tree parts.

1. Find words in the next layer
2. The length of the sortest ladder
3. The number of ladders

Let's say the length of each word is m and the number of words is n.

1. m characters that can be changed * 26 possible characters * O(1) to check if the word is in the wordList = O(26m) = O(m).
2. The worst case is that all words in the wordList are used. This makes the time complexity O(n).
3. Every time we look for the next layer of words, it is possible to find 26m in the next layer. However this is only for the first half of the ladder because we flip front and back. Hence there could be up to O((26m)<sup>n/2</sup>) possible ladders.

Combine thses tree parts, it is O(m * n * (26m)<sup>n/2</sup>).

The space complexity could be up to O((26m)<sup>n/2</sup>) which is all possible ladders.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [String](https://leetcode.com/tag/string/) , [Backtracking](https://leetcode.com/tag/backtracking/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) 

## Similar Questions

[Word Ladder](https://leetcode.com/problems/word-ladder/)
