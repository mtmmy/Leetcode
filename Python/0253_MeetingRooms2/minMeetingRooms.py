import unittest
import heapq
import collections

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        d = collections.defaultdict(int)

        for i in intervals:
            d[i.start] += 1
            d[i.end] -= 1
        
        result, room = 0, 0

        for key in sorted(d):
            val = d[key]
            room += val
            result = max(result, room)
        
        return result
        
    def minMeetingRooms2(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        h = []
        heapq.heapify(h)
        
        for interval in intervals:
            if h and h[0] <= interval.start:
                heapq.heappop(h)
            heapq.heappush(h, interval.end)
            
        return len(h)

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(1, target.minMeetingRooms([Interval(7, 10), Interval(2, 4)]))
        self.assertEqual(2, target.minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))

if __name__ == '__main__':
    unittest.main()    
        