using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class RemoveNthNodeFromEndOfList {
        public ListNode Solution(ListNode head, int n) {

            var pre = head;
            var cur = head;
            var step = 0;
            
            while (step < n && cur != null) {
                cur = cur.next;
                step++;
            }
            
            if (cur == null) {
                head = head.next;
                return head;
            }
                
            while (cur.next != null) {
                pre = pre.next;
                cur = cur.next;
            }
            
            var temp = pre.next;
            pre.next = temp.next;
            return head;

        }
    }
}
