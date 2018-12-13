import unittest
import time

class Solution:    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lenS, lenP = len(s), len(p)
        i, j, s_star, p_star = 0, 0, 0, -1
        while i < lenS:
            if j < lenP and (s[i] == p[j] or p[j] == '?'):
                i ,j = i + 1, j + 1
            elif j < lenP and p[j] == '*':
                s_star, p_star = i, j
                j += 1
            elif p_star != -1:
                s_star += 1
                i, j = s_star, p_star + 1
            else:
                return False

        while j < lenP and p[j] == '*':
            j += 1

        return True if j == lenP else False

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return 1

        m, n = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    continue
                if j == 0:
                    dp[i][j] = p[i - 1] == "*" and dp[i - 1][0]
                else:
                    if p[i - 1] == "?":
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[i - 1] == "*":
                        dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j - 1] and s[j - 1] == p[i - 1]                  
        
        return dp[-1][-1]

        

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(True, target.isMatch("acbccbcdef", "*b?*f"))
        self.assertEqual(False, target.isMatch("aab", "c*a*b"))
        self.assertEqual(False, target.isMatch("aa", "a"))
        self.assertEqual(True, target.isMatch("aa", "aa"))
        self.assertEqual(True, target.isMatch("cb", "?b"))
        self.assertEqual(False, target.isMatch("cb", "?a"))
        self.assertEqual(True, target.isMatch("adceb", "*a*b"))
        self.assertEqual(False, target.isMatch("acdcb", "a*c?b"))

if __name__ == '__main__':
    unittest.main()
    
        