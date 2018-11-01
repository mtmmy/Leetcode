# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals)

## Description

Given a collection of intervals, merge all overlapping intervals.

Example 1:

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

Example 2:

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
```

## Solution

First we sort intervals by their starts. Secondly, we iterate the interval array. We use two variables to keep a combined intervals starts from the start and end of the first interval. Afterward we iterate the array and compare the original interval and the combined intervals:  

1. If the start of the orignal interval is smaller than the end of the combined interval and the end of the original interval is greater or equal to the end of the combined interval, we replace the end of the combined interval by the end of the original interval. It means we merge them.  
2. Else if the end of the original interval is smaller than the end of the combined interval, which means the combined interval has already covered the range of the original interval, we do nothing.  
3. Otherwise we keep this new combined interval to our result array and update the combined interval with the original interval.

Since the interation part is just O(n) and the sorting part is O(nlogn), the total time complexity is O(nlogn).

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Sort](https://leetcode.com/tag/sort/) 

## Similar Questions

[Insert Interval](https://leetcode.com/problems/insert-interval/), [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/), [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/), [Teemo Attacking](https://leetcode.com/problems/teemo-attacking/), [Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/), [Range Module](https://leetcode.com/problems/range-module/), [Employee Free Time](https://leetcode.com/problems/employee-free-time/), [Partition Labels](https://leetcode.com/problems/partition-labels/)
