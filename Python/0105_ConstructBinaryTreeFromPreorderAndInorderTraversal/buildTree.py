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
            curNode = TreeNode(inorder[idx])
            curNode.left = self.buildTree(preorder, inorder[0:idx])
            curNode.right = self.buildTree(preorder, inorder[idx+1:])
            return curNode

target = Solution()
target.buildTree([3,9,20,15,7], [9,3,15,20,7])