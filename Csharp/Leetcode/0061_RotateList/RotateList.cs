using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class RotateList {
        public ListNode Solution(ListNode head, int k) {
            var nodesCount = CountNodes(head);
        
            if (nodesCount > 0 && k >= nodesCount) {
                k = k % nodesCount;
            }
            
            if (nodesCount <= 1 || k == 0) {
                return head;
            }
            
            head = Rotate(head, k);
            return head;
        }
        
        private int CountNodes(ListNode head) {
            var count = 0;
            var curNode = head;
            while (curNode != null) {
                curNode = curNode.next;
                count++;
            }
            return count;
        }
        
        private ListNode Rotate(ListNode head, int k) {
            var leading = head;
            var tracking = head;
            
            while (k > 0) {
                leading = leading.next;
                k--;
            }
            
            while (leading.next != null) {
                leading = leading.next;
                tracking = tracking.next;
            }
            
            leading.next = head;
            head = tracking.next;
            tracking.next = null;
            
            return head;
        }
    }
}
