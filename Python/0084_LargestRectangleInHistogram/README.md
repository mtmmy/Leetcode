# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram)

## Description

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

![image](https://leetcode.com/static/images/problemset/histogram.png)

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 

![image](https://leetcode.com/static/images/problemset/histogram_area.png)

The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

```
Input: [2,1,5,6,2,3]
Output: 10
```

## Solution

We use a stack to store the index value one by one if the height of the current index is greater than that of the last index in the stack. Once we confront the condition that the current height is greater than the height of the last index in the stack, we use the last element in the stack as the pivot to calculate the area that is formed by histograms on the left side. Because the current histogram reduces the height of the rectagle, we need calculate areas by higher histogram first. 

So we keep poping out the last histogram and calculate the rectangle formed by its height untill we confront a histogram which is shorter than the current one. Since histogram on the left-hand side is absolutely shorter than the last histogram, the left boundry is the last histogram in the stack and right boundry is the current histogram. By keep doing this process, we can calculate all rectangles formed by each histogram and find the maximum one.

The time complexity and auxiliary space are both O(N) because we need to go through the array once and use a stack to store indices of the array.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Stack](https://leetcode.com/tag/stack/) 

## Similar Questions

[Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
