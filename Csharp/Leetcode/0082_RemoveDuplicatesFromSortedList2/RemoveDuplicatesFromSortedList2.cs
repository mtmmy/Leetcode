using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class RemoveDuplicatesFromSortedList2 {
        public ListNode Solution(ListNode head) {
            if (head == null) {
                return head;
            }

            var curNode = head;
            ListNode tempNode = null;

            while (curNode != null && curNode.next != null) {
                if (curNode.val != curNode.next.val) {
                    tempNode = curNode;
                    curNode = curNode.next;
                } else {
                    var sameNode = curNode;
                    var nodeVal = sameNode.val;
                    while (sameNode != null && sameNode.val == nodeVal) {
                        sameNode = sameNode.next;
                    }
                    if (tempNode == null) {
                        head = sameNode;
                        curNode = head;
                    } else {
                        tempNode.next = sameNode;
                        curNode = tempNode;
                    }
                }
            }

            return head;
        }
    }
}
