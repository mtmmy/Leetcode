class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        n = len(word)
        if n not in self.root:
            self.root[n] = set([word])
        else:
            self.root[n].add(word)
            

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """        
        n = len(word)
        if n not in self.root:
            return False
        if "." not in word:
            return word in self.root[n]
        
        for vocabulary in self.root[n]:
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