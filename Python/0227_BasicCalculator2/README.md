# [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii)

## Description

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

```
Input: "3+2*2"
Output: 7
```

Example 2:

```
Input: " 3/2 "
Output: 1
```

Example 3:

```
Input: " 3+5 / 2 "
Output: 5
```

Note:

- You may assume that the given expression is always valid.
- Do not use the eval built-in library function.

## Solution

We use a sign to keep the last operator we met. And use a stack to store numbers. There are four kinds of operators, we do the different operations as follows:

```
if sign == "+":
    stack.append(num)
elif sign == "-":
    stack.append(-num)
elif sign == "*":
    stack[-1] *= num
elif sign == "/":
    if stack[-1] ^ num < 0 and stack[-1] % num != 0:                        
        stack[-1] = stack[-1] // num + 1
    else:
        stack[-1] //= num
```

"+" and "-" are straightforward. We just push numbers with corresponding signs. "\*" is also simple, we need to calculate operand of "\*" before "+" and "-", so we pick the top element from the stack, doing the multiplication and push the result back into the stack. Only the division has a special case we need to consider which is when the quotient is negetive and division is divisable and we use "//" operator, we get the closest smaller integer to the quotient thus we need plus one under this situation. Here we use XOR to check if the quotient is negative and modulo to check if the division is divisable.

Time complexity: O(n)<br>
Space complexity: O(n)

## Related Topics

[String](https://leetcode.com/tag/string/) 

## Similar Questions

[Basic Calculator](https://leetcode.com/problems/basic-calculator/), [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/), [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)
