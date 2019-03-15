# [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii)

## Description

Given two arrays, write a function to compute their intersection.

Example 1:

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

Example 2:

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

Note:

- Each element in the result should appear as many times as it shows in both arrays.
- The result can be in any order.

Follow up:

- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


## Solution

Solution 1:

We use a hash table to store the appearance of each number in **nums1**. And we go through nums2 to check if the current number is in the hash table and its counting is greater than 0. If so, we add that number in the result.

Time complexity: O(n)<br>
Space complexity: O(n)

```
counter = collections.Counter(nums1)        
result = []
for num in nums2:
    if num in counter and counter[num] > 0:
        result.append(num)
        counter[num] -= 1
    
return result
```

Solution 2 (arrays are sorted):

We use two pointers for each array. Sourcecode tells the story.

```
i, j = 0, 0
result = []
while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        result.append(nums1[i])
        i += 1
        j += 1
    elif nums1[i] < nums2[j]:
        i += 1
    else:
        j += 1
return result
```

Follow up 1:<br>
We just use solution two which helps up save the space since we don't need to create a hash table.

Follow up 2:<br>
We build the hash map on nums1 becasue it costs less space.

Follow up 3:<br>
We build the hash map on nums1 and load nums2 in batches.

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) , [Binary Search](https://leetcode.com/tag/binary-search/) , [Sort](https://leetcode.com/tag/sort/) 

## Similar Questions

[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
