using Leetcode.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class MergedTwoSortedList {
        public ListNode Solution(ListNode l1, ListNode l2) {

            // recursive solution
            if (l1 == null) {
                return l2;
            }

            if (l2 == null) {
                return l1;
            }

            if (l1.val < l2.val) {
                l1.next = Solution(l1.next, l2);
                return l1;
            } else {
                l2.next = Solution(l1, l2.next);
                return l2;
            }

            // iterative solution
            //if (l1 == null && l2 == null) {
            //    return null;
            //} else if (l1 == null) {
            //    return l2;
            //} else if (l2 == null) {
            //    return l1;
            //}

            //ListNode head = null; ;
            //ListNode cur = null;

            //if (l1.val <= l2.val) {
            //    head = new ListNode(l1.val);
            //    l1 = l1.next;
            //} else {
            //    head = new ListNode(l2.val);
            //    l2 = l2.next;
            //}
            //cur = head;

            //while (l1 != null || l2 != null) {
            //    if (l1 == null) {
            //        cur.next = l2;
            //        break;
            //    } else if (l2 == null) {
            //        cur.next = l1;
            //        break;
            //    } else if (l1.val <= l2.val) {
            //        cur.next = new ListNode(l1.val);
            //        l1 = l1.next;
            //    } else {
            //        cur.next = new ListNode(l2.val);
            //        l2 = l2.next;
            //    }
            //    cur = cur.next;
            //}
            //return head;
        }
    }
}
