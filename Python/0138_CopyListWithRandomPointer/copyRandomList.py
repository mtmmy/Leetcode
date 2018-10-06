# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return head
        
        curNode = head
        while curNode is not None:
            copyNode = RandomListNode(curNode.label)
            copyNode.next = curNode.next
            curNode.next = copyNode
            curNode = copyNode.next
            
        curNode = head
        while curNode is not None:            
            if curNode.random is not None:
                curNode.next.random = curNode.random.next
            curNode = curNode.next.next
            
        curNode = head
        copyNode = curNode.next
        result = curNode.next
        while copyNode.next is not None:
            curNode.next = curNode.next.next
            curNode = curNode.next            
            
            copyNode.next = copyNode.next.next
            copyNode = copyNode.next

        curNode.next = curNode.next.next
        
        return result