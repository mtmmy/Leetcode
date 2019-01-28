# [172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes)

## Description

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

```
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```

Example 2:

```
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```

Note: Your solution should be in logarithmic time complexity.

## Solution

We get a trailing zero when multiplying by 10, which is 2 x 5. Since 2s are much more than 5s, we just count how many 5s in the factorial sequence. The following example is 25! and totally we have 6 5s in the sequence.

```
1 x ... x 5 x ... x (2 x 5) x ... x (3 x 5) x ...... x (5 x 5)
```

Time complexity: O(n)<br>
Space complexity: O(1)

## Related Topics

[Math](https://leetcode.com/tag/math/) 

## Similar Questions

[Number of Digit One](https://leetcode.com/problems/number-of-digit-one/), [Preimage Size of Factorial Zeroes Function](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/)
