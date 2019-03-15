class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m, n, deletes = len(A), len(A[0]), 0
        toCompare = [True] * m
        
        for i in range(n):
            tempCompare = toCompare[:]
            for j in range(m - 1):
                if toCompare[j]:
                    if A[j][i] > A[j + 1][i]:
                        deletes += 1
                        toCompare = tempCompare
                        break
                    elif A[j][i] < A[j + 1][i]:
                        toCompare[j] = False
        return deletes