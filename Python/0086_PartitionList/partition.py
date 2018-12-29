class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        greater, smaller = ListNode(-1), ListNode(-1)
        gHead, sHead = greater, smaller
        cur = head
        
        while cur:
            if cur.val < x:
                smaller.next = cur
                smaller = smaller.next
            else:
                greater.next = cur
                greater = greater.next
            cur = cur.next
        
        greater.next = None
        smaller.next = gHead.next
        return sHead.next