using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode {
    public class ListNode {
        public int val;
        public ListNode next;
        public ListNode(int x) { val = x; }

        public override bool Equals(object obj) {
            var toCompareWith = obj as ListNode;
            var compare = this;

            if (toCompareWith == null) {
                return false;
            } else {
                while(compare.next != null) {
                    if (compare.val == toCompareWith.val && toCompareWith.next != null) {
                        compare = compare.next;
                        toCompareWith = toCompareWith.next;
                    } else {
                        return false;
                    }
                }
                return true;
            }
        }
    }
}
