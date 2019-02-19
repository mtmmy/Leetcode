# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        hashTable = collections.defaultdict(dict)
        
        def dfs(node, posX, posY):
            if not node:
                return
            if posY not in hashTable[posX]:
                hashTable[posX][posY] = [node.val]
            else:
                hashTable[posX][posY].append(node.val)            
            dfs(node.left, posX - 1, posY - 1)
            dfs(node.right, posX + 1, posY - 1)
        
        dfs(root, 0, 0)
        result = []
        for key in sorted(hashTable):
            temp = []
            for innerKey in sorted(hashTable[key], key=lambda x : -x):
                temp += sorted(hashTable[key][innerKey])
            result.append(temp)
            
        return result