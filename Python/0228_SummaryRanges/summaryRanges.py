from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def toString(self):
        if self.start == self.end:
            return str(self.start)
        return "{}->{}".format(self.start, self.end)
        
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        intervals = []
        begin, cur = nums[0], nums[0]
        for num in nums:
            if num - cur > 1:
                intervals.append(Interval(begin, cur))
                begin = num
                cur = num
            else:
                cur = num
        intervals.append(Interval(begin, cur))
        return [interval.toString() for interval in intervals]