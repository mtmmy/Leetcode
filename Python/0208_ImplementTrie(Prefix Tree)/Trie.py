class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        # create a trie node for each letter hierarchically
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p[1] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            if c not in p:
                return False
            p = p[c]
        return 1 in p

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            if c not in p:
                return False
            p = p[c]
        return True

if __name__ == '__main__':
    target = Trie()
    target.insert("apple")
    target.search("apple")
    target.search("app")
    target.startsWith("app")
    target.insert("app")
    target.search("app")