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
            var used = Enumerable.Repeat(false, vals.Count).ToList();
            used[0] = true;
            var root = new TreeNode(Int32.Parse(vals[0]));
            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);

            for (int i = 0; i < vals.Count; i++) {
                var curNode = queue.Dequeue();
                var firstTwo = FirstTwoUnusedVal(used);
                if (firstTwo[0] >= 0) {
                    used[firstTwo[0]] = true;
                    if (vals[firstTwo[0]] == "null") {
                        curNode.left = null;
                    } else {
                        curNode.left = new TreeNode(Int32.Parse(vals[firstTwo[0]]));
                        queue.Enqueue(curNode.left);
                    }
                } else {
                    break;
                }

                if (firstTwo[1] >= 0) {
                    used[firstTwo[1]] = true;
                    if (vals[firstTwo[1]] == "null") {
                        curNode.right = null;
                    } else {
                        curNode.right = new TreeNode(Int32.Parse(vals[firstTwo[1]]));
                        queue.Enqueue(curNode.right);
                    }
                }
            }

            return root;
        }

        private List<int> FirstTwoUnusedVal(List<bool> used) {
            var result = new List<int>();
            for (int i = 0; i < used.Count; i++) {
                if (result.Count == 2) {
                    break;
                }
                if (used[i] == false) {
                    result.Add(i);
                }
            }

            for (int i = result.Count; i < 2; i++) {
                result.Add(-1);
            }

            return result;
        }
    }
}
