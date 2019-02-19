# [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii)

## Description

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
```

Example 2:

```
Input: [[7,10],[2,4]]
Output: 1
```

## Solution

Solution 1:

We maintain a hash, at the key of a starting time, we increase value with 1. In ending time, we decrese with 1. This move means we assign a room when an interval starts and releas a room when an interval ends. After building up a hash from all intervals, we sort this map by key and accumulate their values. The maximum value during the accumulation is the minimum required rooms.

Time complexity: O(n log n) for sorting<br>
Space complexity: O(n)

Solution 2:

We first sort intervals by their start value in the ascending order. And we maintain a min heap to store end values of intervals. We pop the value when the start value of later inteveals is not less than the min value in the heap. This gesture implys that these two interval are compatible which they can be arranged in the same room. After running through intervals, the corresponding intervals of end values in the heap all need rooms at the same time. Hence the size of the heap is the minimum number of rooms required.

Time complexity: O(n log n) with n intervals and log n for the worse case of insertion and deletion from the heap.<br>
Space compelxity: O(n) worst case of the size of the heap

## Related Topics

[Heap](https://leetcode.com/tag/heap/) , [Greedy](https://leetcode.com/tag/greedy/) , [Sort](https://leetcode.com/tag/sort/) 

## Similar Questions

[Merge Intervals](https://leetcode.com/problems/merge-intervals/), [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/), [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
