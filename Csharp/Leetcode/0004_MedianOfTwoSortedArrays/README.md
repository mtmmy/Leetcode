# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)

## Description

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```



Example 2:

```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```



## Solution
We generate a findKth function to help up looking for the median recursively. For simplicity, we first check the length of two lists, if A is longer, we flip over to make sure B is always not shorter than A. If A is zero, we simply return the kth number in B. 

And then we reach the core of the devide and conquer. We first get an index of A , idxA, which is the minimum of k/2 and length of A, and an index of B which is k - idxA. Then we compare A[idxA - 1] and B[idxB - 1] we have three outcomes.

1. A[idxA - 1] < B[idxB - 1]: this means numbers in A[0] to A[idx - A] will be less than the median so we can dump them.
2. A[idxA - 1] > B[idxB - 1]: similar with above only we dump B[0] to B[idxB - 1]
3. A[idxA - 1] == B[idxB - 1]: We found the median.

Everytime we enter the recursive function, we cut the input to half. So the time complexity of the solution is O(log(m + n)).