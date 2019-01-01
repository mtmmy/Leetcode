class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m < 1 or m > n or not head:
            return None
        
        cur, pre = head, None

        for _ in range(m - 1):
            pre = cur
            cur = cur.next
        
        endFirst, startSecond = pre, cur        
        pre = cur
        cur = cur.next

        for _ in range(n - m):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        startSecond.next = cur
        if m == 1:
            return pre

        endFirst.next = pre        
        return head