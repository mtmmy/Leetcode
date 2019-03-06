class Solution:        
    def longestOnes(self, A, K: int) -> int:
        result, j = 0, 0
        for i in range(len(A)):
            if A[i] == 0:
                K -= 1
            if K < 0:
                if A[j] == 0:
                    K += 1
                j += 1
            result = max(result, i - j + 1)
        return result
                