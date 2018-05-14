using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Tools {
	
    public class ListNode {
		
        public int val;
        public ListNode next;
        public ListNode() { val = 0;  }
        public ListNode (int x) { val = x; }

        /// <summary>
        /// Initializes a new instance of the <see cref="T:Leetcode.Tools.ListNode"/> class.
        /// </summary>
        /// <param name="nums">Nums.</param>
        public ListNode(int[] nums) {
            var curNode = this;
            for (int i = 0; i < nums.Length; i++) {
                curNode.val = nums[i];

                if (i != nums.Length - 1) {
                    curNode.next = new ListNode();
                    curNode = curNode.next;
                }
            }
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="T:Leetcode.Tools.ListNode"/> class.
        /// </summary>
        /// <param name="s">Input String. The format should be "1, 2, 3, 4, 5"</param>
        public ListNode(string s) : this(s.Split(',').Select(c => Int32.Parse(c.Trim())).ToArray()) {
        }

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
