# [212. Word Search II](https://leetcode.com/problems/word-search-ii)

## Description

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

```
Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
```

Note:
You may assume that all inputs are consist of lowercase letters a-z.

## Solution

We create a trie based on the words list first and we use recursive function to detect if the word is in the trie. Use board[0][0] as an example. We check if the first layer of the trie contains 'o' and it does so we go to the next recursion. We first check board[1][0] which is 'e' and we check if the child layer of 'o' in the trie contains 'e' or not and it doesn't so this path ends. The other path is board[0][1] which is 'a' and the children layer of 'o' contains 'a' so we keep going on this path.

After we find the word 'oath' in the board, we put the word into the result list and delete this word from trie in case we add duplicates.

m = len(board), n = len(board[0]), w = len(words), l = words average length

Time complexity: O(w * l + m * n * l * 4<sup>l</sup>)<br>
w * l is the time we generate the trie; m * n is the time we spend on going through the board; l is the time we seach the word in the trie; 4<sup>l</sup> is the time for recursion.

Space compelxity: O(w * l + l) where w * l is used for the trie and l is the size of the stack of the recursion.

## Related Topics

[Backtracking](https://leetcode.com/tag/backtracking/) , [Trie](https://leetcode.com/tag/trie/) 

## Similar Questions

[Word Search](https://leetcode.com/problems/word-search/)
