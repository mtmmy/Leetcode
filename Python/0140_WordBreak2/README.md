# [140. Word Break II](https://leetcode.com/problems/word-break-ii)

## Description

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:

```
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
```

Example 2:

```
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
```

Example 3:

```
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
```

## Solution

We can use recursion to solve this problem. Take Exapmle 1 to explain, the idea is, for the string "catsanddog", we know we can start with "cat" and "cats" and the next step is that runs the same algorithm on strings "sanddog" and "anddog". We can get all possible sentences by finishing this recursive algorithm.

We can also observe that we may run the algorithm on the same substrings multiple times. What we can do is that we use a hash to save the result of these substrings and save executing time.

For the time complexity, we can use this example to analyse:

```
s = "aaaaaaa......"
wordDict = ["a", "aa", "aaa", "aaaa", ......]
```

For this example, the recurence relations is as follows:

```
T(n) = T(n - 1) + T(n - 2) + .... T(1)
```

Which will result in O(2<sup>n</sup>). And the space complexity is the same.


## Related Topics

[Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Word Break](https://leetcode.com/problems/word-break/), [Concatenated Words](https://leetcode.com/problems/concatenated-words/)
