import unittest
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        words = []
        specials = "!?',;. "
        tempWord = ""
        for s in paragraph.lower():
            if s in specials:
                if tempWord and tempWord not in banned:
                    words.append(tempWord)
                tempWord = ""
            else:
                tempWord += s
        if tempWord:
            words.append(tempWord)
        return Counter(words).most_common(1)[0][0]
        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual("ball", target.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
        self.assertEqual("the", target.mostCommonWord("abc abc? abcd the jeff!", ["abc","abcd","jeff"]))

if __name__ == '__main__':
    unittest.main()