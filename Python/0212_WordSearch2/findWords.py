import unittest

class TrieNode:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]        
        node["#"] = word
    
    def delete(self, word):
        def dfs(children, position):
            if position == len(word):
                del children['#']
                return
            dfs(children[word[position]], position+1)
            if not children[word[position]]:
                del children[word[position]]
        dfs(self.root, 0)

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """        
        if not board or not words or not board[0]:
            return []
        
        result = []
        trie = TrieNode()
        for word in words:
            trie.insert(word)        
            
        def search(trieNode, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in trieNode:
                return
            
            temp = board[i][j]
            newTrie = trieNode[temp]
            if "#" in newTrie:
                result.append(newTrie["#"])
                trie.delete(newTrie["#"])
            
            board[i][j] = "*"
            
            search(newTrie, i - 1, j)
            search(newTrie, i + 1, j)
            search(newTrie, i, j - 1)
            search(newTrie, i, j + 1)
                    
            board[i][j] = temp
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                search(trie.root, i, j)
        
        return result