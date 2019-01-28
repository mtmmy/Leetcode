# [204. Count Primes](https://leetcode.com/problems/count-primes)

## Description

Count the number of prime numbers less than a non-negative number, n.

Example:

```
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```

## Solution

We can use [Sieve of Eratosthenes algorithm](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to find primes efficiently. Here is the visualization of the algorithm:

![](https://leetcode.com/static/images/solutions/Sieve_of_Eratosthenes_animation.gif)

Time complexity: O(n log log n)<br>
Space compelxity: O(n)

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Math](https://leetcode.com/tag/math/) 

## Similar Questions

[Ugly Number](https://leetcode.com/problems/ugly-number/), [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/), [Perfect Squares](https://leetcode.com/problems/perfect-squares/)
