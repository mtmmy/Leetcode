class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        
        total = 0
        for j in range(len(A[0])):
            for i in range(1, len(A)):
                if A[i][j] < A[i-1][j]:
                    total += 1
                    break
        
        return total