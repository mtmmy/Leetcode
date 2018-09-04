package com.leetcode._0237_DeleteNodeInALinkedList;

import com.leetcode.utils.ListNode;

public class DeleteNodeInALinkedList {
    public void solution(ListNode node) {

        node.val = node.next.val;
        node.next = node.next.next;
    }
}
