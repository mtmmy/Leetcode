class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[0:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root