class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 1:
            return len(A)
        
        compareNext = [0] * len(A)
        
        for i in range(1, len(A)):
            compareNext[i - 1] = 1 if A[i] < A[i - 1] else 0 if A[i] == A[i - 1] else -1
        
        count, maxLen = 1, 0
        
        for i in range(1, len(compareNext)):
            if compareNext[i - 1] == -compareNext[i]:
                count += 1
            else:
                maxLen = max(count, maxLen)
                count = 1
        
        return maxLen + 1