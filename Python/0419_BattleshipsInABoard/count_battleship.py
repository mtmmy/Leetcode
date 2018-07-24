class Solution:
    def countBattleships(self, board): 
        """
        :type board: List[List[str]]
        :rtype: int
        """       
        height = len(board)

        if height == 0:
            return 0

        width = len(board[0])
        count = 0
        for i in range (0, height, 1):
            for j in range (0, width, 1):
                if board[i][j] == "X":
                    adjacentX = i > 0 and board[i - 1][j] == "X"
                    adjacentY = j > 0 and board[i][j - 1] == "X"
                    if not adjacentX and not adjacentY:
                        count += 1
        return count

if __name__ == "__main__":
    target = Solution()
    board = []
    board.append(["X",".",".","X"])
    board.append([".",".",".","X"])
    board.append([".",".",".","X"])
    print(target.countBattleships(board))