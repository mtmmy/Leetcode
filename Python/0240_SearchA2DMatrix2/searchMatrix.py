import unittest

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if not matrix or not matrix[0]:
        #     return False
        
        # for row in matrix:
        #     left, right = 0, len(row) - 1
        #     while left < right:
        #         mid = (left + right) // 2                
        #         if row[mid] > target:
        #             right = mid - 1
        #         elif row[mid] < target:
        #             left = mid + 1
        #         else:
        #             return True
        #     if row[left] == target:
        #         return True
        # return False
        if not matrix or not matrix[0]:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
        
        return False

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(True, target.searchMatrix([[1, 1]], 1))
        self.assertEqual(False, target.searchMatrix([[1, 1]], 0))
        test = [
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertEqual(True, target.searchMatrix(test, 5))
        self.assertEqual(False, target.searchMatrix(test, 20))

if __name__ == '__main__':
    unittest.main()    
        