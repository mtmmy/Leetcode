# [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive)

## Description

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

```
Input: [1,2,0]
Output: 3
```

Example 2:

```
Input: [3,4,-1,1]
Output: 2
```

Example 3:

```
Input: [7,8,9,11,12]
Output: 1
```

Note:

Your algorithm should run in O(n) time and uses constant extra space.

## Solution

To solve the problem, we can rearrange the number list to:

```
num[i] = i + 1 for all i > 0
```

for example, **num[0] = 1, num[1] = 2**. After rearranging, we go through the list and the first element that **num[i] != i + 1** is the place that we miss the first postive number. Hence **i + 1** is the number.

The rearranging takes O(n) and the searching takes O(n) as well. Totally, it's O(n).

## Related Topics

[Array](https://leetcode.com/tag/array/) 

## Similar Questions

[Missing Number](https://leetcode.com/problems/missing-number/), [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/), [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/), [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/)
