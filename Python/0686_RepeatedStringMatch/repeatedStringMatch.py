class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        m, n = len(A), len(B)
        lower = -(-n // m)       #ceil(n, m)
        
        if B in (A * lower):
            return lower
        
        if B in (A * (lower + 1)):
            return lower + 1
        
        return -1