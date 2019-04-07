from typing import List
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        
        def update(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or A[i][j] == 0:
                return
            A[i][j] = 0
            update(i - 1, j)
            update(i + 1, j)
            update(i, j - 1)
            update(i, j + 1)
            
        for i in range(m):
            update(i, 0)
            update(i, n - 1)
        for j in range(n):
            update(0, j)
            update(m - 1, j)
            
        return sum([sum(row[1:-1]) for row in A[1:-1]])
            