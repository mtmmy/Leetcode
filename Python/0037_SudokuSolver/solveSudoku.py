class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """        
        def findUnassigned():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        return r, c
            return -1, -1
        
        def isValid(row, col, num):
            return num not in board[row] and isColValid(col, num) and isBoxValid(row, col, num)
        
        def isColValid(col, num):
            for i in range(9):
                if board[i][col] == num:
                    return False
            return True
        
        def isBoxValid(row, col, num):
            boxRow = row - row % 3
            boxCol = col - col % 3
            for i in range(boxRow, boxRow + 3):
                for j in range(boxCol, boxCol + 3):
                    if board[i][j] == num:
                        return False
            return True
        
        def solver():
            row, col = findUnassigned()
            if row == -1:
                return True
            
            for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if isValid(row, col, num):
                    board[row][col] = num
                    if solver():
                        return True
                    board[row][col] = "."
            return False
        solver()