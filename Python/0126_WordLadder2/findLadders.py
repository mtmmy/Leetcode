import unittest
import string
from collections import deque
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        word_dict = set(wordList)
        front, back = {beginWord}, {endWord}
        direct = 1
        parents = defaultdict(set)
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                direct *= -1
            next_layer = set()
            word_dict -= front
            for word in front:
                newWords = [word[:i] + c + word[i+1:] for c in string.ascii_letters for i in range(len(beginWord))]
                for newWord in newWords:
                    if newWord in word_dict:
                        next_layer.add(newWord)
                        if direct == 1:
                            parents[newWord].add(word)
                        else:
                            parents[word].add(newWord)
            if next_layer & back:
                result = [[endWord]]
                while result[0][0] != beginWord:
                    result = [[pa] + r for r in result for pa in parents[r[0]]]
                return result
            front = next_layer
        return []
    def findLadders2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer
        return res

    def findLaddersTE(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        result, wordDict, step, paths = [], set(wordList), [beginWord], deque()
        paths.append(step)
        level, minLevel, words = 1, float('inf'), set()

        while paths:
            temp = paths.popleft()
            if len(temp) > level:
                for s in words:
                    if s in wordDict:
                        wordDict.remove(s)
                words.clear()
                level = len(temp)
                if level > minLevel:
                    break
            last = temp[-1]
            for i in range(len(last)):
                newLast = last
                for c in string.ascii_lowercase:
                    newLast = newLast[:i] + c + newLast[i + 1:]
                    if newLast not in wordDict:
                        continue
                    words.add(newLast)
                    nextPath = temp.copy()
                    nextPath.append(newLast)
                    if newLast == endWord:
                        result.append(nextPath)
                        minLevel = level
                    else:
                        paths.append(nextPath)
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([["hit","hot","lot","log","cog"], ["hit","hot","dot","dog","cog"]], target.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

if __name__ == '__main__':
    unittest.main()
        