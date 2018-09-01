import unittest

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
        d = {}

        for i in intervals:
            if i.start in d:
                d[i.start] += 1
            else:
                d[i.start] = 1

            if i.end in d:
                d[i.end] -= 1
            else:
                d[i.end] = -1
        
        result, room = 0, 0

        for key in sorted(d):
            val = d[key]
            room += val
            result = max(result, room)
        
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(1, target.minMeetingRooms([Interval(7, 10), Interval(2, 4)]))
        self.assertEqual(2, target.minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))

if __name__ == '__main__':
    unittest.main()    
        