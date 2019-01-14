import unittest

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        knownDict = {}
        def dfs(subS):
            if subS in knownDict:
                return knownDict[subS]
            if not subS:
                return [""]
            result = []
            for word in wordDict:
                if subS[:len(word)] != word:
                    continue
                memory = dfs(subS[len(word):])
                for m in memory:
                    result.append(word + ("" if not m else " ") + m)
            knownDict[subS] = result
            return knownDict[subS]

        return dfs(s)
        

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        test = ["cat", "cats", "and", "sand", "dog"]
        expected = ["cats and dog","cat sand dog"]
        self.assertCountEqual(expected, target.wordBreak("catsanddog", test))
        
if __name__ == '__main__':
    unittest.main()
        