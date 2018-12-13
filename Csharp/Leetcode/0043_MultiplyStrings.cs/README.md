# [43. Multiply Strings](https://leetcode.com/problems/multiply-strings)

## Description

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

Example 2:

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

Note:

1. The length of both num1 and num2 is < 110.
2. Both num1 and num2 contain only digits 0-9.
3. Both num1 and num2 do not contain any leading zero, except the number 0 itself.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

## Solution

First we create a list whose size is the sum of length of two numbers because the longest length of a product is the length of multiplier and multiplicand combined. We use this array to store products of each place. For example:

```
        1  2  3
     x  4  5  6
   -------------
        6 12 18  <--- 6 is multiplier
     5 10 15     <--- 5 is multiplier
  4  8 12        <--- 4 is multiplier
----------------
0 4 13 28 27 18
```
The bottom line is how the array looks like.

Next, we calculate the carries and the array becomes:

```
[0 5 6 0 8 8]
```

Moreover, we remove all leading zeros and convert the integer array to a string.

THe time complexity is O(mn) where m is the length of one num and n for another. And we need O(m+n) auxiliary space.


## Related Topics

[Math](https://leetcode.com/tag/math/) , [String](https://leetcode.com/tag/string/) 

## Similar Questions

[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/), [Plus One](https://leetcode.com/problems/plus-one/), [Add Binary](https://leetcode.com/problems/add-binary/), [Add Strings](https://leetcode.com/problems/add-strings/)
