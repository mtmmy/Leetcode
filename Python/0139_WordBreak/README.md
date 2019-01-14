# [139. Word Break](https://leetcode.com/problems/word-break)

## Description

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:

```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

Example 2:

```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

Example 3:

```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

## Solution

We use dynamic programming strategy to solve this problem. We create a list **dp** whose length is len(s) + 1 an dp[0] is True. dp[i] denotes whether s[0:i] can be break down by **wordDict**. After that, we use a nested loop to update list under the following condition:

```
if dp[j] and s[j:i] in wordDict:
    dp[i] = True
```

Which means s[0:i] can be break down if s[0:j] can be break down and s[j:i] is the word in the **wordDict**. Thus dp[-1] is whether s can be break down or not.

The time complexity is O(n<sup>2</sup>) and the space complexity is O(n).

## Related Topics

[Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Word Break II](https://leetcode.com/problems/word-break-ii/)
