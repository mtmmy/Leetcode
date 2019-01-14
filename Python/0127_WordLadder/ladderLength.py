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
        front, back = {beginWord}, {endWord}
        wordDict -= front
        step = 0
        
        while front and back:
            step += 1
            if len(front) > len(back):
                front, back = back, front
            s = set()
            for w in front:
                newWords = [w[:i] + c + w[i + 1:] for c in string.ascii_lowercase for i in range(len(beginWord))]
                for newWord in newWords:
                    if newWord in back:
                        return step + 1
                    if newWord not in wordDict:
                        continue
                    wordDict.remove(newWord)
                    s.add(newWord)
            front = s
        return 0

target = Solution()
ans = target.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(ans)