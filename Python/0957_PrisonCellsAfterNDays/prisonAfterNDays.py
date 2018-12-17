class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def getNext(c):
            newC = [0] * 8
            for i in range(1, 7):
                if c[i - 1] == c[i + 1]:
                    newC[i] = 1
                else:
                    newC[i] = 0
            return newC
        
        cells = getNext(cells)
        originalC = cells.copy()
        cells = getNext(cells)
        
        times = 1
        while originalC != cells:
            cells = getNext(cells)
            times += 1
        
        if times == 0:
            return originalC
        
        times = (N - 1) % times
        
        for _ in range(times):
            originalC = getNext(originalC)
        
        return originalC