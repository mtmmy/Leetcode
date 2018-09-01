import unittest

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        result, m, n = 0, len(matrix), len(matrix[0])
        height = [0] * (n + 1)
        for i in range(m):
            stack = []
            for j in range(n + 1):
                if j < n:
                    height[j] = (height[j] + 1) if matrix[i][j] == "1" else 0
                while stack and height[stack[-1]] >= height[j]:
                    cur = stack.pop()
                    result = max(result, height[cur] * (j if not stack else (j - stack[-1] - 1)))
                stack.append(j)
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        test = [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]
        self.assertEqual(6, target.maximalRectangle(test))

if __name__ == '__main__':
    unittest.main()    
        