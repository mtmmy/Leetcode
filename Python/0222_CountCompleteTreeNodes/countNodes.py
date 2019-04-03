# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def getDepth(node, left):
            count = 0
            while node:
                count += 1
                if left:
                    node = node.left
                else:
                    node = node.right
            return count
        
        leftH = getDepth(root, True)
        rightH = getDepth(root, False)
        
        # check if it's complete
        if leftH == rightH:
            return 2 ** leftH - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            