class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.cur = None
        
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        head = Node(-1, None, None)        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if not self.cur:
                head.right = node
                self.cur = node
            else:
                self.cur.right = node
                node.left = self.cur
                self.cur = node            
            dfs(node.right)        
        dfs(root)
        first = head.right
        last = self.cur
        first.left = last
        last.right = first
        return first