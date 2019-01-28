# [189. Rotate Array](https://leetcode.com/problems/rotate-array)

## Description

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

```
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

Example 2:

```
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

Note:

- Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
- Could you do it in-place with O(1) extra space?

## Solution

Solution 1 uses reverse() three times.

```
Input: [1,2,3,4,5,6,7]
1st reverse: [7,6,5,4,3,2,1]
2nd reverse: [5,6,7,4,3,2,1]
3rd reverse: [5,6,7,1,2,3,4]
```
Time compelxity: O(n)<br>
Space complexity: O(1)

Solution 2:

Find the break point directly and tear down the array into two parts. And then merge them in reverse order.

```
Input: [1,2,3,4,5,6,7]
sub array1: [1,2,3,4]
sub array2: [5,6,7]
Output: [5,6,7] + [1,2,3,4] = [5,6,7,1,2,3,4]
```

Time complexity: O(1)<br>
Space complexity: O(n)

## Related Topics

[Array](https://leetcode.com/tag/array/) 

## Similar Questions

[Rotate List](https://leetcode.com/problems/rotate-list/), [Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)
