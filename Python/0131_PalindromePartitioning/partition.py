class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        sLength = len(s)
        result = []
        solution = []
        isPal = [[False] * sLength for i in range(sLength)]
        
        for i in range(sLength - 1, -1, -1):
            for j in range(i, sLength):                
                if (i + 1 >= j - 1 or isPal[i + 1][j - 1]) and s[i] == s[j]:
                    isPal[i][j] = True
        
        self.findPartitions(s, 0, isPal, solution, result)        
        return result
    
    def findPartitions(self, s, start, isPal, solution, result):
        if start == len(s):
            result.append(list(solution))
            return
        
        for i in range(start, len(s)):
            if isPal[start][i]:
                length = i - start + 1
                solution.append(s[start:start + length])
                self.findPartitions(s, i + 1, isPal, solution, result)
                solution.pop()