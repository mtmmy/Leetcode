# [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii)

## Description

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

![image](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

```
Input: 3
Output: [1,3,3,1]
```

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

## Solution

The idea is that we don't need create the whole triangle. We only need to remember the previous row to create the current row. Hence the extra space we need is just **k**.

## Related Topics

[Array](https://leetcode.com/tag/array/) 

## Similar Questions

[Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
