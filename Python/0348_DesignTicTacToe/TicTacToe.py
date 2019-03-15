class TicTacToe:
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal1 = 0
        self.diagonal2 = 0
        self.n = n

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
        score = 1 if player == 1 else -1
        self.rows[row] += score
        self.cols[col] += score
        if row == col:
            self.diagonal1 += score
        if row + col == self.n - 1:
            self.diagonal2 += score
        win = {self.rows[row], self.cols[col], self.diagonal1, self.diagonal2}
        if self.n in win or -self.n in win:
            return player
        return 0