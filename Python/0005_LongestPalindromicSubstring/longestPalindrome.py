class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        n, left, right, length = len(s), 0, 0, 0
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):            
            for j in range(i):
                dp[j][i] = s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1])
                if dp[j][i] and i - j + 1 > length:
                    length = i - j + 1
                    left = j
                    right = i
            dp[i][i] = True

            
        print(dp)
        return s[left:right + 1]
                