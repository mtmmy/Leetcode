package com.leetcode._0445_AddTwoNumbers2;

import com.leetcode.utils.ListNode;

import java.util.Deque;
import java.util.LinkedList;

public class AddTwoNumber2 {
    public ListNode solution(ListNode l1, ListNode l2) {

        Deque<Integer> stack1 = new LinkedList<>();
        Deque<Integer> stack2 = new LinkedList<>();

        ListNode curNode = l1;
        while (curNode != null) {
            stack1.addLast(curNode.val);
            curNode = curNode.next;
        }

        curNode = l2;
        while (curNode != null) {
            stack2.addLast(curNode.val);
            curNode = curNode.next;
        }

        ListNode last = null;
        int sum = 0;
        while (!stack1.isEmpty() || !stack2.isEmpty()) {
            sum += stack1.isEmpty() ? 0 : stack1.pollLast();
            sum += stack2.isEmpty() ? 0 : stack2.pollLast();
            curNode = new ListNode(sum % 10);
            sum /= 10;
            curNode.next = last;
            last = curNode;
        }
        if (sum == 1) {
            ListNode extra = new ListNode(1);
            extra.next = curNode;
            return extra;
        }
        return curNode;
    }
}
