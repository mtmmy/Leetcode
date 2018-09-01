import unittest
from collections import deque

class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        # if not fronts or not backs:
        #     return 0        
        # same = {x for i, x in enumerate(fronts) if x == backs[i]}
        # result = 2001

        # for i in range(len(fronts)):
        #     num1 = fronts[i]
        #     num2 = backs[i]
        #     if num1 != num2:
        #         if num1 not in same:
        #             result = min(result, num1)
        #         if num2 not in same:
        #             result = min(result, num2)
                    
        # return result % 2001

        # same = {x for x, y in zip(fronts, backs) if x == y}
        # nums = [num for num in fronts+backs if num not in same]
        # if len(nums) == 0:
        #     return 0
        # else:
        #     return min(nums)

        res = set(fronts + backs) - set(x for x,y in zip(fronts, backs) if x == y)
        return min(res) if res else 0


class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(2 , target.flipgame([1,2,4,4,7], [1,3,4,1,3]))
        
if __name__ == '__main__':
    unittest.main()
        