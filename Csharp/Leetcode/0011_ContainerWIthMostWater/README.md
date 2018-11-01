# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water)

## Description

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

## Solution

We set two pointers to the head and the tail of the list and calculate the volume of the container and store the maximum volume. After calculating, we compare the height of height[i] and hiegh[j] and move the smaller one. Once i goes over j, we terminate the iteration. Meanwhile, we get the volume of the maximum container. 

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) 

## Similar Questions

[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
