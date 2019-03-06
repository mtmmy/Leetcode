import bisect

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None
                    
class Solution:
    def add(self, node, val):
        curCount = 0
        while 1:
            if val <= node.val:
                node.count += 1
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                curCount += node.count
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
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

    def countSmallerBisect(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []
        
        result, rank = [], []
        
        for num in nums[::-1]:
            i = bisect.bisect_left(rank, num)
            result.append(i)
            rank[i:i] = num,
            
        return result[::-1]
    
    def countSmallerMergeSort(self, nums: 'List[int]') -> 'List[int]':
        result = [0] * len(nums)
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        result[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        
        sort(list(enumerate(nums)))
        return result

# target = Solution()
# target.countSmallerBisect([5,2,6,1])