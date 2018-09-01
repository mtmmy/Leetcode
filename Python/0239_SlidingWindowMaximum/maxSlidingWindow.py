import unittest
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        queue = deque()

        for i in range(len(nums)):
            if len(queue) > 0 and queue[0] == i - k:
                queue.popleft()
            while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result


class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        test = [1,3,-1,-3,5,3,6,7]
        self.assertEqual([3,3,5,5,6,7] , target.maxSlidingWindow(test, 3))
        test = [7,2,4]
        self.assertEqual([7,4] , target.maxSlidingWindow(test, 2))
        
if __name__ == '__main__':
    unittest.main()
        