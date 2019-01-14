# [127. Word Ladder](https://leetcode.com/problems/word-ladder)

## Description

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Note:

Example 1:

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
```

Example 2:

```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```

## Solution

This problem is a simplfied one from [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii). We only need to find the length of the shortest sequence. We also set up front and back and keep updating them and force them going toward to the middle of the sequece with counting the number of words. Once front and back intersect, we find the ladder and return its length.

For the time complexity, we can use the one we show in [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii). We can ignore the third part because we only need one sequece to get the shortest length. Hence the time complexity is O(m * n) where m is the length of each word is and n is the number of words. The space complexity is the possible largest size of **newWords** which is O(26m). 

## Related Topics

[Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) 

## Similar Questions

[Word Ladder II](https://leetcode.com/problems/word-ladder-ii/), [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)
