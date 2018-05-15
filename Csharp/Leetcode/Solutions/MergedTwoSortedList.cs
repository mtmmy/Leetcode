using Leetcode.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class MergedTwoSortedList {
        public ListNode MergeTwoLists(ListNode l1, ListNode l2) {

            ListNode head = null; ;
            ListNode cur = null;

            if (l1 == null && l2 == null) {
                return head;
            }

            if (l1 == null) {
                head = new ListNode(l2.val);
                l2 = l2.next;
            } else if (l2 == null) {
                head = new ListNode(l1.val);
                l1 = l1.next;
            } else if (l1.val <= l2.val) {
                head = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                head = new ListNode(l2.val);
                l2 = l2.next;
            }
            cur = head;

            while (l1 != null || l2 != null) {

                if (l1 == null) {
                    cur.next = new ListNode(l2.val);
                    l2 = l2.next;
                } else if (l2 == null) {
                    cur.next = new ListNode(l1.val);
                    l1 = l1.next;
                } else if (l1.val <= l2.val) {
                    cur.next = new ListNode(l1.val);
                    l1 = l1.next;
                } else {
                    cur.next = new ListNode(l2.val);
                    l2 = l2.next;
                }
                cur = cur.next;
            }
            return head;
        }
    }
}
