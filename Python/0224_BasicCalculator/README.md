# [224. Basic Calculator](https://leetcode.com/problems/basic-calculator)

## Description

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

```
Input: "1 + 1"
Output: 2
```

Example 2:

```
Input: " 2-1 + 2 "
Output: 3
```

Example 3:

```
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

Note:

- You may assume that the given expression is always valid.
- Do not use the eval built-in library function.

## Solution

Solution 1:

We use a stack to store elements in the input. Once we hit the right parentheses, we find the last left parentheses and calculate the formula in between immediately and push the answer to the stack.

Time complexity: O(n)<br>
Space complexity: O(n)

Solution 2:

We use two stacks for numbers and operators separately. We calculate the formula along with going thorugh the input string. We use a value **sign** (1 or -1) to remember what the operator we meet and use it to multiply numbers. Once we meet a left parentheses, we push the answer so far into the number stack and the current **sign** value to the operator stack and calculate the answer within parentheses first. When we hit a right parentheses, we pop out the answer and the operator and add them to the answer within parentheses following by multiplying.

Time complexity: O(n)<br>
Space complexity: O(n)

Even though two solutions have the same time complexity, solution 1 can be up to O(2n) which is still higher than solution 2 which is just O(n).

## Related Topics

[Math](https://leetcode.com/tag/math/) , [Stack](https://leetcode.com/tag/stack/) 

## Similar Questions

[Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/), [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/), [Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/), [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/), [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)
