using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class ReverseNodesInKGroup {
        public ListNode ReverseKGroup(ListNode head, int k) {

            if (head == null || k == 1) {
                return head;
            }

            var root = new ListNode(-1);

            var previousLast = root;
            var thisPeriodHead = head;
            ListNode nextPeriodHead = null;
            ListNode thisPeriodLast = null;

            while (true) {

                bool isLastPeriod = false;
                var cur = thisPeriodHead;
                for (int i = 0; i < k - 1; i++) {
                    if (cur == null || cur.next == null) {
                        isLastPeriod = true;
                        break;
                    }                    
                    cur = cur.next;                    
                }
                thisPeriodLast = cur;

                if (isLastPeriod) {
                    if (root.next == null) {
                        root.next = head;
                    }
                    break;
                }
                nextPeriodHead = thisPeriodLast.next;
                cur.next = null;
                ListNode tempNode = null;
                tempNode = thisPeriodHead;
                thisPeriodHead = Reverse(thisPeriodHead);
                previousLast.next = thisPeriodHead;
                thisPeriodLast = tempNode;
                previousLast = thisPeriodLast;
                thisPeriodLast.next = nextPeriodHead;
                thisPeriodHead = nextPeriodHead;
            }

            return root.next;
        }

        private ListNode Reverse(ListNode head) {

            var root = new ListNode(-1);
            root.next = head;
            var cur = head;
            ListNode pre = null;
            ListNode next = null;

            while (cur != null) {
                next = cur.next;
                cur.next = pre;
                pre = cur;
                cur = next;
            }

            return pre;
        }
    }
}
