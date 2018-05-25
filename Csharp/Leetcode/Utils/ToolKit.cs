using System;
using System.Collections.Generic;
using System.Linq;

namespace Leetcode.Utils {
    public class ToolKit {

        public ListNode GenerateListNode(int[] nums) {
            if (nums.Length == 0) {
                return null;
            }

            var curNode = new ListNode();
            var head = curNode;
            for (int i = 0; i < nums.Length; i++) {
                curNode.val = nums[i];

                if (i != nums.Length - 1) {
                    curNode.next = new ListNode();
                    curNode = curNode.next;
                }
            }
            return head;
        }

        public ListNode GenerateListNode(string s) {
            var nums = s.Split(',').Select(c => Int32.Parse(c.Trim())).ToArray();
            return GenerateListNode(nums);
        }

        /// <summary>
        /// Take a string list and return the root of a binary tree.
        /// </summary>
        /// <returns>The tree node.</returns>
        /// <param name="vals">String list that contains numbers or the string "null."</param>
        public TreeNode GenerateTreeNode(List<string> vals) {
            
            if (vals.Count == 0 || vals[0] == "null") {
                return null;
            }
            var i = 0;
            TreeNode node2;
            var node1 = new TreeNode(Int32.Parse(vals[i++]));
            var queue = new Queue<TreeNode>();
            queue.Enqueue(node1);
            var root = node1;

            while (queue.Count > 0) {
                node1 = queue.Dequeue();
                if (i < vals.Count) {
                    var val = vals[i++];
                    if (val != "null") {
                        node2 = new TreeNode(Int32.Parse(val));
                        queue.Enqueue(node2);
                        node1.left = node2;
                    }
                }

                if (i < vals.Count) {
                    var val = vals[i++];
                    if (val != "null") {
                        node2 = new TreeNode(Int32.Parse(val));
                        queue.Enqueue(node2);
                        node1.right = node2;
                    }
                }
            }

            return root;
        }
    }
}
