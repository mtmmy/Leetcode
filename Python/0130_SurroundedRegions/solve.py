class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        width, length = len(board), len(board[0])
        
        def dfs(board, i, j):
            if board[i][j] == 'O':
                board[i][j] = 'a'
                if i > 0:
                    dfs(board, i - 1, j)
                if i < width - 1:
                    dfs(board, i + 1, j)
                if j > 0:
                    dfs(board, i, j - 1)
                if j < length - 1:
                    dfs(board, i, j + 1)
        
        for i in range(width - 1):
            if board[i][0] == 'O':
                dfs(board, i, 0)
        for i in range(length - 1):
            if board[-1][i] == 'O':
                dfs(board, width - 1, i)
        for i in range(width - 1, -1, -1):
            if board[i][-1] == 'O':
                dfs(board, i, length - 1)
        for i in range(length -1, -1, -1):
            if board[0][i] == 'O':
                dfs(board, 0, i)
        
        for i in range(width):
            for j in range(length):
                if board[i][j] == 'a':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'