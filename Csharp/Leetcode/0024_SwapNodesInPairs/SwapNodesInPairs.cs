using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class SwapNodesInPairs {
        public ListNode SwapPairs(ListNode head) {

            var root = new ListNode(-1);
            root.next = head;
            var cur = root;

            while (cur.next != null && cur.next.next != null) {
                var first = cur.next;
                var second = cur.next.next;

                first.next = second.next;
                cur.next = second;
                second.next = first;
                
                cur = cur.next.next;
            }

            return root.next;
        }
    }
}
