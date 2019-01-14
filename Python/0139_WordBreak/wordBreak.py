import unittest

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True        

        for i in range(1, length + 1):
            for j in range(i):
                 if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]
        

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(False, target.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
        self.assertEqual(True, target.wordBreak("leetcode", ["leet", "code"]))
        self.assertEqual(True, target.wordBreak("applepenapple", ["apple", "pen"]))

if __name__ == '__main__':
    unittest.main()