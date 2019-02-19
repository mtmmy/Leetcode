# [247. Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii)

## Description

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

```
Input:  n = 2
Output: ["11","69","88","96"]
```

## Solution

We use backtracking to append and prepend numbers to strings. For each recursion, we do the following steps:

```
if curLength == 0:
    return [""]
elif curLength == 1:
    return ["0", "1", "8"]
else:
    result = []
    subArrays = self.fillup(curLength - 2, length)
    
    for a in subArrays:
        if curLength != length:
            result.append("0" + a + "0")
        result.append("1" + a + "1")
        result.append("6" + a + "9")
        result.append("8" + a + "8")
        result.append("9" + a + "6")
    return result
```

Two terminate condition is length of 0 and 1. For 0, we only need to return an empty string for the following appending and prepending. For 1, we initilize it with 3 numbers that fulfill strobogrammatic numbers which are 0, 1, and 8. If the length is greater than 1, we start append and prepend strings with valid numbers. The special case is when the curLength not yet reached total length, we need to append 0s since the result can't not contain leading 0s.

Time complexity: O(5<sup>n</sup>). Because we create 5 times of string for each recursion.<br>
Space complexity: O(5<sup>n</sup>). Same as the time complexity.


## Related Topics

[Math](https://leetcode.com/tag/math/) , [Recursion](https://leetcode.com/tag/recursion/) 

## Similar Questions

[Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/), [Strobogrammatic Number III](https://leetcode.com/problems/strobogrammatic-number-iii/)
