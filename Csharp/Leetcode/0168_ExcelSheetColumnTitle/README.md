# [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title)

## Description

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```

Example 1:

```
Input: 1
Output: "A"
```

Example 2:

```
Input: 28
Output: "AB"
```

Example 3:

```
Input: 701
Output: "ZY"
```

## Solution

We can consider it as base-26 number system (but not exactly), where A is 0 and Z is 25. However, there is a slightly different from a real number system which is when the number carries over, the new digit start from 0 (A in base-26). So we need to minus one every time we reach the new digit. 
    
Time complexity: O(n)<br>
Space complexity: O(1)

## Related Topics

[Math](https://leetcode.com/tag/math/) 

## Similar Questions

[Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)
