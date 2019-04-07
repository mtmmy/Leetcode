# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def toNumber(node, num):
            if not node:
                return 0
            num = num * 2 + node.val
            if not node.left and not node.right:
                return num
            total = toNumber(node.left, num) + toNumber(node.right, num)
            return total % (10 ** 9 + 7)
        return toNumber(root, 0)