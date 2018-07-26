class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False

        i, j = 0, 0
        while matrix[i][-1] < target:
            i += 1
            if i == len(matrix):
                return False
        
        while matrix[i][j] < target:
            j += 1
            if j == len(matrix[i]):
                return False
                
        return target == matrix[i][j]
        
if __name__ == "__main__":
    target = Solution()
    matrix = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]
    print(target.searchMatrix(matrix, 3))
    print(target.searchMatrix(matrix, 13))
    print(target.searchMatrix(matrix, 50))