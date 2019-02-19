# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:    
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        if not root:
            return ""
        left = self.smallestFromLeaf(root.left)
        right = self.smallestFromLeaf(root.right)
        return (left if not right or left and left <= right else right) + chr(97 + root.val)
    
    def smallestFromLeaf2(self, root: 'TreeNode') -> 'str':
        letters = "abcdefghijklmnopqrstuvwxyz"
        result = [""]
        
        def dfs(node, string):
            if not node:
                return ""
            if not node.left and not node.right:
                string += letters[node.val]
                result[0] = string[::-1] if not result[0] else min(result[0], string[::-1])
            else:
                string += letters[node.val]
                dfs(node.left, string)
                dfs(node.right, string)
        
        dfs(root, "")
        return result[0]
        
target = Solution()
root = TreeNode(1)
root.right = TreeNode(2)

result = target.smallestFromLeaf(root)
print(result)