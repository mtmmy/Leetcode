import unittest

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(M, used, student):
            if used[student]:
                return 0
            used[student] = 1
            for i in range(len(M[student])):
                if M[student][i] == 1:
                    dfs(M, used, i)
            return 1

        if not M:
            return 0
        m = len(M)
        if m == 0:
            return 0
        
        used = [0] * m
        circles = 0
        for i in range(m):
            if dfs(M, used, i) == 1:
                circles += 1
        return circles

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        test = [[1,1,0],[1,1,0],[0,0,1]]
        self.assertEqual(2, target.findCircleNum(test))
        test = [[1,1,0],[1,1,1],[0,1,1]]
        self.assertEqual(1, target.findCircleNum(test))
        
if __name__ == '__main__':
    unittest.main()
        