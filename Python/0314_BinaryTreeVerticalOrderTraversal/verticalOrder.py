# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict, deque
from typing import List
class Solution:
    def verticalOrderBFS(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        verticalLayer = defaultdict(list)
        queue = deque([(0, root)])
        
        while queue:
            nextLevel = []
            while queue:
                level, cur = queue.popleft()
                if cur.left:
                    nextLevel.append((level - 1, cur.left))
                if cur.right:
                    nextLevel.append((level + 1, cur.right))
                verticalLayer[level].append(cur.val)
            queue += nextLevel
        
        return [verticalLayer[key] for key in sorted(verticalLayer)]
    
    def verticalOrderDFS(self, root: TreeNode) -> List[List[int]]:
        verticalLayer = defaultdict(dict)
                
        def dfs(node, vLv, hLv):
            if not node:
                return
            if hLv in verticalLayer[vLv]:
                verticalLayer[vLv][hLv].append(node.val)
            else:
                verticalLayer[vLv][hLv] = [node.val]
            
            dfs(node.left, vLv - 1, hLv + 1)
            dfs(node.right, vLv + 1, hLv + 1)
        
        dfs(root, 0, 0)
        result = []
        for c in sorted(verticalLayer):
            temp = []
            for r in sorted(verticalLayer[c]):
                temp += verticalLayer[c][r]
            result.append(temp)
        return result