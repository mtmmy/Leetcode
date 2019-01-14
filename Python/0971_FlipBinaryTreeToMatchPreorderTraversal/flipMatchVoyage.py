class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        result = []
        
        def dfs(cur):
            if not cur:
                return True
            if cur.val != voyage[0]:
                return False
            voyage.pop(0)
            if cur.left and cur.left.val != voyage[0]:
                result.append(cur.val)
                cur.left, cur.right = cur.right, cur.left
            return dfs(cur.left) and dfs(cur.right)
        
        return result if dfs(root) else [-1]