class TicTacToe:

    board = []
    player1ToWin = []
    player2ToWin = []
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [[0] * n for _ in range(n)]
        self.player1ToWin = []
        self.player2ToWin = []
        set(self.player1ToWin)
        set(self.player2ToWin)


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        board = self.board
        n = len(board)
        toWin = self.player1ToWin if player == 1 else self.player2ToWin
        
        if (row, col) in toWin:
            return player
        
        board[row][col] = player
        self.removeToWin(row, col)
        
        self.setToWin(row, col, player)
        return 0
        
    
    def setToWin(self, row, col, player):
        toWin = self.player1ToWin if player == 1 else self.player2ToWin
        board = self.board
        n = len(board)
        
        zeroCount = 0
        toWinPos = (-1, -1)
        for i in range(n):
            if board[row][i] == 0:
                toWinPos = (row, i)
                zeroCount += 1
                if zeroCount > 1:
                    toWinPos = (-1, -1)
                    break
            elif board[row][i] != player:
                toWinPos = (-1, -1)
                break
            else:
                continue
        if toWinPos != (-1, -1):
            toWin.append(toWinPos)
        
        zeroCount = 0
        toWinPos = (-1, -1)
        for i in range(n):
            if board[i][col] == 0:
                toWinPos = (i, col)
                zeroCount += 1
                if zeroCount > 1:
                    toWinPos = (-1, -1)
                    break
            elif board[i][col] != player:
                toWinPos = (-1, -1)
                break
            else:
                continue
        if toWinPos != (-1, -1):
            toWin.append(toWinPos)
            
    
        zeroCount = 0
        toWinPos = (-1, -1)
        for i in range(n):
            if board[i][i] == 0:
                toWinPos = (i, i)
                zeroCount += 1
                if zeroCount > 1:
                    toWinPos = (-1, -1)
                    break
            elif board[i][i] != player:
                toWinPos = (-1, -1)
                break
            else:
                continue
        if toWinPos != (-1, -1):
            toWin.append(toWinPos)


        zeroCount = 0
        toWinPos = (-1, -1)
        for i in range(n):
            if board[i][n - i - 1] == 0:
                toWinPos = (i, n - i - 1)
                zeroCount += 1
                if zeroCount > 1:
                    toWinPos = (-1, -1)
                    break
            elif board[i][n - i - 1] != player:
                toWinPos = (-1, -1)
                break
            else:
                continue
        if toWinPos != (-1, -1):
            toWin.append(toWinPos)

    def removeToWin(self, row, col):
        if (row, col) in self.player1ToWin:
            self.player1ToWin.remove((row, col))
        if (row, col) in self.player2ToWin:
            self.player2ToWin.remove((row, col))