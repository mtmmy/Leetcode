# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number)

## Description

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

```
Input: [1,3,4,2,2]
Output: 2
```

Example 2:

```
Input: [3,1,3,4,2]
Output: 3
```

Note:

1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n2).
4. There is only one duplicate number in the array, but it could be repeated more than once.

## Solution

If we transfrom the array into the linked list as follows:

```
array: [1,3,4,2,2]
linked list: 1 -> 3 -> 2 -> 4
                       ^    |
                       +----+
Every element is a node and the value is its pointer represents the target, e.g. nums[0] = 1 points to nums[1] = 3
```
The problem is exactly like [142. Linked List Cycle II](https://github.com/mtmmy/Leetcode/tree/master/Java/Leetcode/src/main/java/com/leetcode/_0142_LinkedListCycle2).

Time complexity: O(n)<br>
Space complexity: O(1)

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) , [Binary Search](https://leetcode.com/tag/binary-search/) 

## Similar Questions

[First Missing Positive](https://leetcode.com/problems/first-missing-positive/), [Single Number](https://leetcode.com/problems/single-number/), [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/), [Missing Number](https://leetcode.com/problems/missing-number/), [Set Mismatch](https://leetcode.com/problems/set-mismatch/)
