# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left and root.val != root.left.val:
            return False
        if root.right and root.val != root.right.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)