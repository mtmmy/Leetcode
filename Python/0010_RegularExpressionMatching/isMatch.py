class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
                
        dp = [[False] * (n + 1) for _ in range(m + 1) ]
        dp[0][0] = True
        
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != "*" and p[j - 1] != ".":
                    dp[i][j] = i > 0 and s[i - 1] == p[j - 1] and dp[i - 1][j - 1]
                elif p[j - 1] == ".":
                    dp[i][j] = i > 0 and dp[i - 1][j - 1]
                elif j > 1:
                    dp[i][j] = (dp[i][j - 2]) or (i > 0 and dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == "."))

        return dp[m][n]
                
                
        