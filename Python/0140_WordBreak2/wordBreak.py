import unittest

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        knownDict = {}
        def dfs(s, wordDict):
            if s in knownDict:
                return knownDict[s]
            if len(s) == 0:
                return [""]
            result = []
            for word in wordDict:
                if s[:len(word)] != word:
                    continue
                memory = dfs(s[len(word):], wordDict)
                for string in memory:
                    result.append(word + ("" if len(string) == 0 else " ") + string)
            knownDict[s] = result
            return knownDict[s]

        return dfs(s, wordDict)
        

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        test = ["cat", "cats", "and", "sand", "dog"]
        expected = ["cats and dog","cat sand dog"]
        self.assertCountEqual(expected, target.wordBreak("catsanddog", test))
        
if __name__ == '__main__':
    unittest.main()
        