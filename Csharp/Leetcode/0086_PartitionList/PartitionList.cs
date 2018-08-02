using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class PartitionList {
        public ListNode Solution(ListNode head, int x) {

            ListNode equalorgreater = new ListNode(-1);
            ListNode smaller = new ListNode(-1);

            var egCount = equalorgreater;
            var sCount = smaller;

            var curNode = head;

            while (curNode != null) {
                if (curNode.val < x) {
                    sCount.next = curNode;
                    curNode = curNode.next;
                    sCount = sCount.next;
                    sCount.next = null;
                } else {
                    egCount.next = curNode;
                    curNode = curNode.next;
                    egCount = egCount.next;
                    egCount.next = null;
                }
            }

            sCount.next = equalorgreater.next;

            return smaller.next;
        }
    }
}
