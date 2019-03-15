# [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays)

## Description

Given two arrays, write a function to compute their intersection.

Example 1:

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

Example 2:

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

Note:

- Each element in the result must be unique.
- The result can be in any order.

## Solution

We convert two arrays into sets and run the & operation on them to find the intersection.

Time complexity: O(n)<br>
Space complexity: O(n)

```
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return list(set(nums1) & set(nums2))
```

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) , [Binary Search](https://leetcode.com/tag/binary-search/) , [Sort](https://leetcode.com/tag/sort/) 

## Similar Questions

[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
