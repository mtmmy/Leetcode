class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        firstRow = False
        firstCol = False
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
        
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0

        if firstRow:
            for j in range(n):
                matrix[0][j] = 0

if __name__ == "__main__":
    target = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    result = target.setZeroes(matrix)
    print(result)