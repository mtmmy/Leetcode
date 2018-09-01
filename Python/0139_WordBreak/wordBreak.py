import unittest

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == None or wordDict == None:
            return False
        
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True        

        for i in range(1, length + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[length]

        # matched = []
        
        # for w in wordDict:
        #     if w == s:
        #         return True
        #     n = len(w)
        #     if s[0:n] == w:
        #         matched.append(w)
        
        # for m in matched:
        #     if m == s:
        #         return True
        #     l = len(m)
        #     tempS = s[l:]
        #     for w in wordDict:
        #         n = len(w)
        #         if tempS[0:n] == w:
        #             newM = m + w
        #             matched.append(newM)
        
        # return False
                    
        
        

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(False, target.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
        self.assertEqual(True, target.wordBreak("leetcode", ["leet", "code"]))
        self.assertEqual(True, target.wordBreak("applepenapple", ["apple", "pen"]))

if __name__ == '__main__':
    unittest.main()