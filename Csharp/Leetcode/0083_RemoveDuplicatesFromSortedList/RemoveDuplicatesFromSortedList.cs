using System;
using Leetcode.Utils;
namespace Leetcode.Solutions {
    public class RemoveDuplicatesFromSortedList {
        public ListNode Solution(ListNode head) {
            if (head == null) {
                return head;
            }
            
            var cur = head;
            var next = cur.next;

            while (next != null) {
                if (next.val == cur.val) {
                    next = next.next;
                    cur.next = null;
                } else {
                    cur.next = next;
                    cur = next;
                    next = next.next;
                }
            }

            return head;
        }
    }
}
