# [528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight)

## Description

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1. 1 <= w.length <= 10000
2. 1 <= w[i] <= 10^5
3. pickIndex will be called at most 10000 times.

Example 1:

```
Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
```

Example 2:

```
Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
```

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

## Solution

## Related Topics

[Binary Search](https://leetcode.com/tag/binary-search/) , [Random](https://leetcode.com/tag/random/) 

## Similar Questions

[Random Pick Index](https://leetcode.com/problems/random-pick-index/), [Random Pick with Blacklist](https://leetcode.com/problems/random-pick-with-blacklist/), [Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/)
