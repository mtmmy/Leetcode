package com.leetcode._0143_ReorderList;

import com.leetcode.utils.ListNode;

public class ReorderList {
    public void solution(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        boolean isEven = true;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        if (fast != null) {
            isEven = false;
            slow = slow.next;
        }

        slow = reverse(slow);
        fast = head;

        while (slow != null && fast != null) {
            ListNode nextFast = fast.next;
            ListNode nextSlow = slow.next;

            if (slow == nextFast) {
                slow.next = null;
                break;
            }

            if (!isEven && slow == nextFast.next) {
                nextFast.next = null;
                fast.next = slow;
                slow.next = nextFast;
                break;
            }

            fast.next = slow;
            slow.next = nextFast;

            fast = nextFast;
            slow = nextSlow;
        }
        System.out.println("");
    }

    public ListNode reverse(ListNode head) {
        ListNode preNode = null;
        ListNode nextNode = null;

        while (head != null) {
            nextNode = head.next;
            head.next = preNode;
            preNode = head;
            head = nextNode;
        }
        return preNode;
    }
}
