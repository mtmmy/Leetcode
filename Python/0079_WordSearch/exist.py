class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False

        n = len(board[0])
        if n == 0:
            return False
        
        for i in range(m):
            for j in range(n):
                if self.search(board, word, i, j, 0):
                    return True
        return False

    def search(self, board, word, row, col, level):
        if level == len(word):
            return True

        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[level]:
            return False

        curChar = board[row][col]
        board[row][col] = "0"
        if self.search(board, word, row - 1, col, level + 1):
            return True
        if self.search(board, word, row + 1, col, level + 1):
            return True
        if self.search(board, word, row, col - 1, level + 1):
            return True
        if self.search(board, word, row, col + 1, level + 1):
            return True
        board[row][col] = curChar
        return False

if __name__ == "__main__":
    target = Solution()
    board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    print(target.exist(board, "ABCCED"))
    print(target.exist(board, "ABCB"))