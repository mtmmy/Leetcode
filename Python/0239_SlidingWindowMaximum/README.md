# [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum)

## Description

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

```
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

## Solution



## Related Topics

[Heap](https://leetcode.com/tag/heap/) 

## Similar Questions

[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/), [Min Stack](https://leetcode.com/problems/min-stack/), [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/), [Paint House II](https://leetcode.com/problems/paint-house-ii/)
