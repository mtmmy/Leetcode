# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

## Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## Solution

We use backtracking algorithm to solve this problem. The purpose of using it is we can get all combinations and meanwhile we can ignore those invalid ones. 

We set up a recursive functions and the terminal condition is the length of the string reaches 2n which means we have equal numbers of left and right parentheses. Besides the terminal condition, we have two conditions. One is when the number of left parentheses has not yet reached the n, we call another recursive function. The other is calling the recursive function when the number of right parentheses is less than the amount of left parentheses. By doing these two conditions, we can guarentee that the parentheses are indeed valid bacause the right parenthese is always comes after the left ones and will be filled up to the amount of left parenthese.

Total operation times can be written as:

```
T(n) = 2T(n - 1) + 1 = 2^n - 1
O(T(n)) = O(2^n)
```
The time complexity is O(2^n). And the space complexity is O(n) which comes from log(2^n). 

## Related Topics

[String](https://leetcode.com/tag/string/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/), [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
