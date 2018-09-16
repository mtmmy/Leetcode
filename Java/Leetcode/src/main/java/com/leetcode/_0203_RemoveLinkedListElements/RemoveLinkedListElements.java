package com.leetcode._0203_RemoveLinkedListElements;

import com.leetcode.utils.ListNode;

public class RemoveLinkedListElements {
    public ListNode solution(ListNode head, int val) {

        ListNode newHead = new ListNode(val - 1);
        newHead.next = head;

        ListNode curNode = newHead;
        ListNode preNode = null;

        while (curNode != null) {
            if (curNode.val == val) {
                preNode.next = curNode.next;
            } else {
                preNode = curNode;
            }
            curNode = curNode.next;
        }

        return newHead.next;
    }
}
