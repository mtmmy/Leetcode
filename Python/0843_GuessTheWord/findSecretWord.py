import unittest

class Master:
    def __init__(self, secretWord):
        self.secretWord = secretWord

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        if word == self.secretWord:
            return 6
        else:
            return sum(c1 == c2 for c1, c2 in zip(word, self.secretWord))

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def pairMatches(word1, word2):
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))

        def mostSimilarWord():
            counts = [[0] * 26 for _ in range(6)]
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord("a")] += 1
            
            bestScore = 0
            for word in candidates:
                score = 0
                for i, c in enumerate(word):
                    score += counts[i][ord(c) - ord("a")]
                if score > bestScore:
                    bestScore = score
                    bestWord = word
            return bestWord

        candidates = wordlist[:]
        while candidates:
            simWord = mostSimilarWord()
            matches = master.guess(simWord)

            if matches == 6:
                return 6
            
            candidates = [word for word in candidates if pairMatches(simWord, word) == matches]


class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        master = Master("acckzz")
        target = Solution()
        test = ["acckzz","ccbazz","eiowzz","abcczz"]
        self.assertEqual(6, target.findSecretWord(test, master))
        

if __name__ == '__main__':
    unittest.main()
        