import unittest

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start, end = newInterval.start, newInterval.end
        left, right = [], []

        for interval in intervals:
            if interval.end < start:
                left.append(interval)
            elif interval.start > end:
                right.append(interval)
            else:
                start = min(start, interval.start)
                end = max(end, interval.end)
        return left + [Interval(start, end)] + right
        