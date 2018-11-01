class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        m, n = len(name), len(typed)
        
        dp = [[False] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(i, n):
                if i == 0:
                    dp[i][j] = name[i] == typed[j]
                else:
                    dp[i][j] = name[i] == typed[j] and (dp[i - 1][j - 1] or dp[i][j - 1])

        return dp[-1][-1]
            
        