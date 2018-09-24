class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self, list1, list2):
        dummy = ListNode(0)
        
        cur = dummy
        ptr1 = list1
        ptr2 = list2
        
        while cur:                
            if ptr1.val < ptr2.val:
                cur.next = ptr1
                ptr1 = ptr1.next
            else:
                cur.next = ptr2
                ptr2 = ptr2.next
            if cur.next:
                cur = cur.next
                
        if not ptr1:
            cur.next = ptr2
        if not ptr2:
            cur.next = ptr1
        
        return dummy.next
            
    def split(self, head):
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next        
        
        temp = slow
        slow = slow.next
        temp.next = None
        fast = head
        
        return self.merge(self.split(fast), self.split(slow))
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.split(head)

solution = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
solution.sortList(head)