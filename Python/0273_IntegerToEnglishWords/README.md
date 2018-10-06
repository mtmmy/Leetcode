# [273. Integer to English Words](https://leetcode.com/problems/integer-to-english-words)

## Description

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^{31} - 1.

Example 1:

```
Input: 123
Output: "One Hundred Twenty Three"
```

Example 2:

```
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```

Example 3:

```
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

Example 4:

```
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

## Solution

This is a tedious problem. The key is taking care details. We use a recursive function to get the number of each digit and its decimal units. Nothin special.