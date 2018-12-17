# [57. Insert Interval](https://leetcode.com/problems/insert-interval)

## Description

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

Example 2:

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

## Solution

Since intervals have been sorted, we can start from the first one and seperate intervals into three parts. One part of intervals are those whose end time are earlier than the new interval. We gather these intervals to the **left** array. Another part of intervals are those whose start time is behind the end time of the new interval and we put these intervals to the **right** array. The reset intervals are obviously overlaped with the new interval, so we merge them into one. The last thing we need to do is simply combining these three parts of intervals.

The time complexity and the space complexity are both O(N).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Sort](https://leetcode.com/tag/sort/) 

## Similar Questions

[Merge Intervals](https://leetcode.com/problems/merge-intervals/), [Range Module](https://leetcode.com/problems/range-module/)
