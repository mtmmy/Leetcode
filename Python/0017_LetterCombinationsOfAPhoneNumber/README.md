# [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)

## Description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![image](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

Example:

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

## Solution

Maintain a result list and keep adding all possible characters to the end of existing string. Like the provided example, first, we have ["a", "b", "c"]. And at the next iteration, we add all possible characters ["d", "e", "f"] to the existing stirng so the exsiting stirngs become ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Let say the average characters that one button contains is m and the length of the input digit is n, the time complexity is O(m^n).

## Related Topics

[String](https://leetcode.com/tag/string/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/), [Combination Sum](https://leetcode.com/problems/combination-sum/), [Binary Watch](https://leetcode.com/problems/binary-watch/)
