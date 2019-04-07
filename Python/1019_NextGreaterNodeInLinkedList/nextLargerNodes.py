from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        temp = []
        cur, i = head, 0
        
        while cur:
            if stack:
                while stack and stack[-1][0] < cur.val:
                    idx = stack.pop()[1]
                    temp.append((cur.val, idx))
            stack.append((cur.val, i))
            cur = cur.next
            i += 1
            
        result = [0] * i
        for val, idx in temp:
            result[idx] = val
        return result