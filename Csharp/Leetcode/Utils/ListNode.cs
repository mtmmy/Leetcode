using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Utils {
	
    public class ListNode {
		
        public int val;
        public ListNode next;
        public ListNode() { }
        public ListNode (int x) { val = x; }

        public override string ToString() {
            var result = "";
            var curNode = this;

            while(curNode != null) {

                result += curNode.val.ToString();

                if (curNode.next != null) {
                    result += ", ";
                }

                curNode = curNode.next;
            }

            return result;
        }
	}
}
