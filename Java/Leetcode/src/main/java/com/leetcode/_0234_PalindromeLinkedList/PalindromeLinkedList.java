package com.leetcode._0234_PalindromeLinkedList;

import com.leetcode.utils.ListNode;

import java.util.Deque;
import java.util.LinkedList;

public class PalindromeLinkedList {
    public boolean solution(ListNode head) {
        Deque<ListNode> stack = new LinkedList<>();
        ListNode curNode = head;
        while(curNode != null) {
            stack.push(curNode);
            curNode = curNode.next;
        }

        curNode = head;
        while(!stack.isEmpty() && curNode != null) {
            if (curNode.val != stack.pop().val) {
                return false;
            }
            curNode = curNode.next;
        }
        return true;
    }

    public boolean solution2(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }


        slow = reverse(slow);

        while (slow != null) {
            if (head.val != slow.val) {
                return false;
            }
            head = head.next;
            slow = slow.next;
        }
        return true;
    }

    private ListNode reverse(ListNode head) {
        ListNode preNode = null;

        while (head != null) {
            ListNode nextNode = head.next;
            head.next = preNode;
            preNode = head;
            head = nextNode;
        }
        return preNode;
    }
}
