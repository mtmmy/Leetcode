import collections
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = collections.defaultdict(list)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.dictionary[len(word)].append(word)
            

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """        
        n = len(word)
        if n not in self.dictionary:
            return False
        if "." not in word:
            return word in self.dictionary[n]
        
        for vocabulary in self.dictionary[n]:
            for i in range(len(word)):
                if word[i] != "." and word[i] != vocabulary[i]:
                    break
            else:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)