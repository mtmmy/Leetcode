# [166. Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal)

## Description

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

```
Input: numerator = 1, denominator = 2
Output: "0.5"
```

Example 2:

```
Input: numerator = 2, denominator = 1
Output: "2"
```

Example 3:

```
Input: numerator = 2, denominator = 3
Output: "0.(6)"
```

## Solution

If we convert fraction to decimal by vertical division, we notice it's recurring when we see a remainder appears the second time. We introduce this idea by using a hash table who stores the position that the remainder appears at the first time. Hence the second time we see that remainder, we know the starting point of the recursion.

Time complexity: O(n)<br>
Space complexity: O(n)

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Math](https://leetcode.com/tag/math/) 