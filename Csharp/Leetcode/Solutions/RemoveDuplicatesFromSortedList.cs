using System;
using Leetcode.Tools;
namespace Leetcode.Solutions {
    public class RemoveDuplicatesFromSortedList {
        public ListNode Solution(ListNode head) {
            var baseline = head;
            var compareWith = baseline.next == null ? null : baseline.next;

            while (compareWith != null) {
                if (compareWith.val == baseline.val) {
                    compareWith = compareWith.next;
                    baseline.next = null;
                } else {
                    baseline.next = compareWith;
                    baseline = compareWith;
                    compareWith = compareWith.next;
                }
            }

            return head;
        }
    }
}
