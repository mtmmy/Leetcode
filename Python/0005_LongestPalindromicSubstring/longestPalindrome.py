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

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, length = 0, 1
        
        for i in range(1, len(s)):
            if i - length >= 1:
                temp = s[i - length - 1:i + 1]  # check odd length
                if temp == temp[::-1]:
                    start = i - length - 1
                    length += 2
                    continue    # if odd length is palindromic, even length is shorter so no need to check
            temp = s[i - length:i + 1]  # check even length
            if temp == temp[::-1]:
                start = i - length
                length += 1
        return s[start:start + length]
                