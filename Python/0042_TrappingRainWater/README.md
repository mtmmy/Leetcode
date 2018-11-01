# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)

## Description

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![image](http://www.leetcode.com/static/images/problemset/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

## Solution

There are two way to solve this problem.

First, we can use the stack.

We iterate the list and push the index of the current number into the stack if the stack is empty or the current number is less or equal to the top of the stack. And when the current number is greater than the number corresponding to the indxe at the top of the stack, there may be a trap.  

We pop the index from the stack which is the bottom of the puddle. The index of two ends of the puddle are the current index and the number at the top of the stack. And we choose the smaller one from them which is the top surface of the puddle; the width is the distance of two ends. And we can get the area of the puddle by height and width.

Time complexity of this solution is O(n).

_________
Secondly, we can solve it by two pointers.

Initially we set pointers at head(left) and tail(right) of the array and keep their values which are previous heights (heightL and heightR). 

If heightL is smaller than heightR, we move left to right with one and compare the current hight of left (height[left]) to the previous height(heightL). If the current height is smaller, it means it must be abble to form a puddle with height of heightL - height[left] because heightL is less than heightR and then we add this height to the grand total of water. If new height isn't less than old height, we simply update old height by new height. 

On the contrary if heightL isn't less than heightR, we do the simliar thing. Once left go over right, we calculate all water.

Time complexity of this solution is O(n) as well.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) , [Stack](https://leetcode.com/tag/stack/) 

## Similar Questions

[Container With Most Water](https://leetcode.com/problems/container-with-most-water/), [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/), [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/), [Pour Water](https://leetcode.com/problems/pour-water/)
