class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A or len(A) < 3:
            return False
        
        if A[0] > A[1] or A[-2] < A[-1]:
            return False
        
        peak = False
        for i in range(0, len(A) - 1):
            if A[i] == A[i + 1]:
                return False
            elif not peak and A[i] > A[i + 1]:
                peak = True
            elif peak and A[i] <= A[i + 1]:
                return False
        return True