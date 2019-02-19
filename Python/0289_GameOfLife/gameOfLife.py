import unittest

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        
        def updateState(i, j):
            lifeNeighbors = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    lifeNeighbors += board[x][y] % 10 if x >= 0 and x < m and y >= 0 and y < n else 0
            lifeNeighbors -= board[i][j] % 10

            if board[i][j] == 1 and (lifeNeighbors == 2 or lifeNeighbors == 3):
                board[i][j] += 10
            if board[i][j] == 0 and lifeNeighbors == 3:
                board[i][j] += 10
        
        for i in range(m):
            for j in range(n):
                updateState(i, j)
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] // 10

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        self.assertEqual(expected, target.gameOfLife(board))

if __name__ == '__main__':
    unittest.main()
        