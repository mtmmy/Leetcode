# [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line)

## Description

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

```
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
```

Example 2:

```
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
```

## Solution

The basic concept is that we find all points which lie on the same line with each nodes. This method totally takes O(n<sup>2</sup>) time. 

The way we confirm two points lie on the same line is to use slope. However if we just use the number of slope, we need taking care too many cases such as divided by zero. Instead we store a tuple which is the irreducible fraction of the slope as a key of a hash and the corresponding value is the amount of points. Futhermore, if the points are duplicates, we can ignore checking the slope and just count them on the same line.

To figure out the irreducible fraction, we need to find the greatest common divisor of numerator and denominator which we build a recursive function to do this.

Time complexity: O(n<sup>2</sup>)<br>Space complexity: O(n)

The reason why the space comlexity is O(n) is that we only need a temporary hash for each point to remember how many points have the same slope and the worst case is every points don't have the same slope value.

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Math](https://leetcode.com/tag/math/) 

## Similar Questions

[Line Reflection](https://leetcode.com/problems/line-reflection/)
