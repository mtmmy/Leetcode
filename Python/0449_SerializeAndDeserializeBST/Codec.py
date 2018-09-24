from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        queue = deque()
        queue.append(root)
        serialized = []
        
        while queue:
            cur = queue.popleft()
            if cur:
                serialized.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                serialized.append("None")
        
        return ",".join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        i, vals = 0, data.split(",")
        n, queue = len(vals), deque()
        root = TreeNode(int(vals[i]))
        queue.append(root)
        i += 1
        
        while queue:
            cur = queue.popleft()
            
            if i < n:
                val = vals[i]
                i += 1
                if val != "None":
                    cur.left = TreeNode(int(val))
                    queue.append(cur.left)
            if i < n:
                val = vals[i]
                i += 1
                if val != "None":
                    cur.right = TreeNode(int(val))
                    queue.append(cur.right)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))