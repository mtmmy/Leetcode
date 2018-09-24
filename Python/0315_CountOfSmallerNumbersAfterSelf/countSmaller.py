class TreeNode:
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None
                    
class Solution:
    def add(self, root, val):
        curCount = 0
        while 1:
            if val <= root.val:
                root.count += 1
                if not root.left:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
            else:
                curCount += root.count
                if not root.right:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
        return curCount
    
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        if not nums:
            return []
        
        root = TreeNode(nums.pop())
        result = [0]
        for val in reversed(nums):
            result.append(self.add(root, val))
            
        return result[::-1]