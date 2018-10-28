class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        
        result = []
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        start, end = intervals[0].start, intervals[0].end
        
        for interval in intervals:
            if interval.start <= end and interval.end >= end:
                end = interval.end                
            elif interval.end < end:
                end = end
            else:
                result.append(Interval(start, end))                
                start = interval.start
                end = interval.end

if __name__ == "__main__":
    target = Solution()
    intervals = []
    
    intervals.append(Interval(12, 15))
    intervals.append(Interval(2, 6))
    intervals.append(Interval(1, 3))    
    intervals.append(Interval(8, 10))
    
    # intervals.append(Interval(1, 4))
    # intervals.append(Interval(2, 3))

    result = target.merge(intervals)