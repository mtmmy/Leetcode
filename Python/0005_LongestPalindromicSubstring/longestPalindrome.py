class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        n, left, length = len(s), 0, 1     
        
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, 0, -1):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = True
                length = 2
                left = i - 1

        for k in range(3, n + 1):
            for i in range(0, n - k + 1):
                j = i + k - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if k > length:
                        length = k
                        left = i

        return s[left : left + length]
                