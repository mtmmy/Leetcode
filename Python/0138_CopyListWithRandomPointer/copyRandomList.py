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
        if not head:
            return head
        
        # copy a node right after each node
        # example: 1 -> 2 -> 3 -> 4
        # after copying: 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4
        curNode = head
        while curNode:
            copyNode = RandomListNode(curNode.label)
            copyNode.next = curNode.next
            curNode.next = copyNode
            curNode = copyNode.next

        # set random pointer of copied node to the copied random target    
        curNode = head
        while curNode:            
            if curNode.random:
                curNode.next.random = curNode.random.next
            curNode = curNode.next.next

        # separate the orignal list and the copied list
        curNode = head
        copyNode = curNode.next
        copiedHead = curNode.next
        while copyNode.next:
            curNode.next = curNode.next.next
            curNode = curNode.next
            copyNode.next = copyNode.next.next
            copyNode = copyNode.next

        curNode.next = curNode.next.next
        
        return copiedHead
