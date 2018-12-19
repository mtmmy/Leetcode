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
        
        start, end = 0, len(matrix) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] < target:
                start = mid + 1
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                return True
        
        row = end
        start, end = 0, len(matrix[row]) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                return True
        
        return False
        
if __name__ == "__main__":
    target = Solution()
    matrix = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]
    print(target.searchMatrix(matrix, 3))
    print(target.searchMatrix(matrix, 13))
    print(target.searchMatrix(matrix, 50))