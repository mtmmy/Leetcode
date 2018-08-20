import unittest
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = paragraph.lower().split(" ")
        d = {}
        mostWord = ""

        for word in words:
            word = word.strip("!?',;.")
            if word not in banned:                
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
                
                if mostWord == "":
                    mostWord = word
                else:
                    if d[word] >= d[mostWord]:
                        mostWord = word
        return mostWord
        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual("ball", target.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
        self.assertEqual("aaaaa", target.mostCommonWord("were abc abc abc abc aaa aaaaa.", ["abc"]))
        self.assertEqual("the", target.mostCommonWord("abc abc? abcd the jeff!", ["abc","abcd","jeff"]))



if __name__ == '__main__':
    unittest.main()