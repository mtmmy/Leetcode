using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class RotateList {
        public ListNode Solution(ListNode head, int k) {
            if (head == null) {
                return null;
            }

            var nodesCount = CountNodes(head);
            var simpleK = k % nodesCount;

            if (simpleK == 0) {
                return head;
            }

            head = RotateOne(head, nodesCount - simpleK);
            return head;
        }

        private int CountNodes(ListNode head) {
            var count = 1;
            var curNode = head;
            while (curNode.next != null) {
                curNode = curNode.next;
                count++;
            }
            return count;
        }

        private ListNode RotateOne(ListNode head, int k) {
            ListNode kthNode;
            var curNode = head;
            for (int i = 0; i < k; i++) {
                ListNode temp = new ListNode();
                if (i + 1 == k) {
                    temp = curNode;
                }
                curNode = curNode.next;
                temp.next = null;
            }
            kthNode = curNode;

            curNode = kthNode;
            ListNode lastNode;
            while (curNode.next != null) {
                curNode = curNode.next;
            }
            lastNode = curNode;
            lastNode.next = head;

            return kthNode;
        }
    }
}
