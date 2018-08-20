import unittest

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # stack = []
        # i, n, water = 0, len(height), 0

        # while i < n:
        #     if len(stack) == 0 or height[i] <= height[stack[-1]]:
        #         stack.append(i)
        #         i += 1
        #     else:
        #         t = stack.pop()
        #         if len(stack) == 0:
        #             continue
        #         water += (min(height[i], height[stack[-1]]) - height[t]) * (i - stack[-1] - 1)
        # return water

        water = 0
        if height is None or len(height) == 0:
            return 0

        i, j = 0, len(height) - 1
        heightL, heightR = height[i], height[j]

        while i < j:
            if heightL < heightR:
                i += 1
                if height[i] < heightL:
                    water += heightL - height[i]
                else:
                    heightL = height[i]
            else:
                j -= 1
                if height[j] < heightR:
                    water += heightR - height[j]
                else:
                    heightR = height[j]                

        return water



class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(1, target.trap([4,2,3]))
        self.assertEqual(2, target.trap([2,0,2]))
        self.assertEqual(6, target.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        self.assertEqual(27, target.trap([9,1,4,0,2,8,6,3,5]))


if __name__ == '__main__':
    unittest.main()