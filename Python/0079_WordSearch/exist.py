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

        used = [[False] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if self.search(board, word, used, (i, j), 0):
                    return True
        return False

    def search(self, board, word, used, curPos, index):
        if index == len(word):
            return True
        row = curPos[0]
        col = curPos[1]

        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or used[row][col] or board[row][col] != word[index]:
            return False

        used[row][col] = True
        if self.search(board, word, used, (row - 1, col), index + 1):
            return True
        if self.search(board, word, used, (row + 1, col), index + 1):
            return True
        if self.search(board, word, used, (row, col - 1), index + 1):
            return True
        if self.search(board, word, used, (row, col + 1), index + 1):
            return True
        used[row][col] = False
        return False

if __name__ == "__main__":
    target = Solution()
    board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    print(target.exist(board, "ABCCED"))
    print(target.exist(board, "ABCB"))