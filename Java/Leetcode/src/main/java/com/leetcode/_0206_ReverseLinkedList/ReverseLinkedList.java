package com.leetcode._0206_ReverseLinkedList;

import com.leetcode.utils.ListNode;

public class ReverseLinkedList {
    public ListNode solution(ListNode head) {

        ListNode curNode = head;
        ListNode nextNode = null;
        ListNode preNode = null;

        while (curNode != null) {
            nextNode = curNode.next;
            curNode.next = preNode;
            preNode = curNode;
            curNode = nextNode;
        }

        return preNode;
    }
}
