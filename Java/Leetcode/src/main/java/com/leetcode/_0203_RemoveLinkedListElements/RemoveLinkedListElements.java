package com.leetcode._0203_RemoveLinkedListElements;

import com.leetcode.utils.ListNode;

public class RemoveLinkedListElements {
    public ListNode solution(ListNode head, int val) {

        ListNode dummy = new ListNode(val - 1);
        dummy.next = head;
        
        ListNode curNode = head;
        ListNode preNode = dummy;
        
        while (curNode != null) {
            if (curNode.val == val) {
                preNode.next = curNode.next;
            } else {
                preNode = curNode;    
            }   
            curNode = curNode.next;
        }
        
        return dummy.next;
    }
}
