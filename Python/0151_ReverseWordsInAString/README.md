# [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string)

## Description

Given an input string, reverse the string word by word.

Example:  

```
Input: "the sky is blue",
Output: "blue is sky the".
```

Note:

- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up: For C programmers, try to solve it in-place in O(1) space.

## Solution

We first reverse the string and use two pointer to traverse the reversed string. We use variable **i** to find the end of a word and **j** denotes the end of the updated part of string. And then we reverse the word to the normal order and append it to the updated part of string. We also use variable **i** to eliminate consecutive spaces to just one.

Time complexity: O(n)<br>Space complexity: O(1)

Python trick:

```
" ".join(s.split()[::-1])
```

We also can accomplish the require by just one line in Python because in split function without giving the separator, it treats consecutive spaces as one separator and gets rid off leading and tailing spaces automatically.


## Related Topics

[String](https://leetcode.com/tag/string/) 

## Similar Questions

[Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)
