import string

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        wordDict = set(wordList)
        length = len(beginWord)
        set1 = {beginWord}
        set2 = {endWord}
        wordDict.remove(endWord)
        step = 0
        
        while len(set1) > 0 and len(set2) > 0:
            step += 1
            if len(set1) > len(set2):
                set1, set2 = set2, set1
            s = set()
            for w in set1:
                newWords = [w[:i] + t + w[i + 1:] for t in string.ascii_lowercase for i in range(length)]
                for newWord in newWords:
                    if newWord in set2:
                        return step + 1
                    if newWord not in wordDict:
                        continue
                    wordDict.remove(newWord)
                    s.add(newWord)
            set1 = s
        return 0