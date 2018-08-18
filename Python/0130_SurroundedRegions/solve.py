class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        if len(board[0]) == 0:
            return
        for i in range(len(board) - 1):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
        for i in range(len(board[-1]) - 1):
            if board[len(board) - 1][i] == 'O':
                self.dfs(board, len(board) - 1, i)
        for i in range(len(board) - 1, -1, -1):
            if board[i][len(board[i]) - 1] == 'O':
                self.dfs(board, i, len(board[i]) - 1)
        for i in range(len(board[0]) -1, -1, -1):
            if board[0][i] == 'O':
                self.dfs(board, 0, i)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'a':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
            
    def dfs(self, board, i, j):
        if board[i][j] == 'O':
            board[i][j] = 'a'
            if i > 0:
                self.dfs(board, i - 1, j)
            if i < len(board) - 1:
                self.dfs(board, i + 1, j)
            if j > 0:
                self.dfs(board, i, j - 1)
            if j < len(board[i]) - 1:
                self.dfs(board, i, j + 1)
                
            
            