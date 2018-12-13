class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dictionary = {}
        for i in range(len(order)):
            dictionary[order[i]] = i
            
        for i in range(0, len(words) - 1):
            for j in range(len(words[i])):
                if len(words[i + 1]) <= j:
                    return False
                if dictionary[words[i][j]] > dictionary[words[i + 1][j]]:
                    return False
                elif dictionary[words[i][j]] < dictionary[words[i + 1][j]]:
                    break
        return True