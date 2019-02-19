import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.highHeap = []
        self.lowHeap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.highHeap and num > self.highHeap[0]:
            heapq.heappush(self.highHeap, num)
        else:
            heapq.heappush(self.lowHeap, -num)
        lows, highs = len(self.lowHeap), len(self.highHeap)
        if lows - highs > 1:
            heapq.heappush(self.highHeap, -heapq.heappop(self.lowHeap))
        elif highs - lows > 1:
            heapq.heappush(self.lowHeap, -heapq.heappop(self.highHeap))
            
    def findMedian(self):
        """
        :rtype: float
        """
        lows, highs = len(self.lowHeap), len(self.highHeap)
        if (lows + highs) & 1: # odd
            return -self.lowHeap[0] if lows > highs else self.highHeap[0]
        else:
            return (-self.lowHeap[0] + self.highHeap[0]) / 2

class MedianFinder2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.nums:
            self.nums.append(num)
        else:
            if self.nums[-1] <= num:
                self.nums.append(num)
            elif self.nums[0] >= num:
                self.nums.insert(0, num)
            else:
                left, right = 0, len(self.nums) - 1
                while 1:
                    mid = (left + right) // 2
                    if right - left == 1:
                        self.nums.insert(right, num)
                        break
                    if self.nums[mid] < num:
                        left = mid
                    elif self.nums[mid] > num:
                        right = mid
                    else:
                        self.nums.insert(mid, num)
                        break
                        
    def findMedian(self):
        """
        :rtype: float
        """        
        if self.nums:
            n = len(self.nums)
            if n % 2 == 0:
                half = n // 2
                return float((self.nums[half] + self.nums[half - 1]) / 2)
            else:
                return float(self.nums[n // 2])

if __name__ == '__main__':
    target = MedianFinder()
    target.addNum(12)
    print(target.findMedian())
    target.addNum(10)
    print(target.findMedian())
    target.addNum(13)
    print(target.findMedian())
    target.addNum(11)
    print(target.findMedian())
    target.addNum(5)
    print(target.findMedian())
    target.addNum(15)
    print(target.findMedian())
    target.addNum(1)
    print(target.findMedian())
    target.addNum(11)
    print(target.findMedian())
    target.addNum(6)
    print(target.findMedian())
    target.addNum(17)
    print(target.findMedian())
    target.addNum(14)
    print(target.findMedian())
    target.addNum(8)
    print(target.findMedian())
    target.addNum(17)
    print(target.findMedian())
    target.addNum(6)
    print(target.findMedian())
    target.addNum(4)
    print(target.findMedian())
    target.addNum(16)
    print(target.findMedian())
    target.addNum(8)
    print(target.findMedian())
    target.addNum(10)
    print(target.findMedian())
    target.addNum(2)
    print(target.findMedian())
    target.addNum(12)
    print(target.findMedian())
    target.addNum(0)
    print(target.findMedian())