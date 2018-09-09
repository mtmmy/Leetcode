import unittest

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not temperatures:
            return []
        
        n = len(temperatures)
        days, stack = [0] * n, []
        
        for i in range(n):            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                days[idx] = i - idx
            stack.append(i)
        return days
            

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([1, 1, 4, 2, 1, 1, 0, 0], target.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

if __name__ == '__main__':
    unittest.main()
        