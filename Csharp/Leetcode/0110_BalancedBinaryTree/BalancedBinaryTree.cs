using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class BalancedBinaryTree {
        public bool IsBalanced(TreeNode root) {
            return DFSDepth(root) != -1;
        }

        private int DFSDepth (TreeNode node) {
            if (node == null) {
                return 0;
            }

            var leftDepth = DFSDepth(node.left);
            if (leftDepth == -1) {
                return -1;
            }
            var rightDepth = DFSDepth(node.right);
            if (rightDepth == -1) {
                return -1;
            }

            if (Math.Abs(leftDepth - rightDepth) > 1) {
                return -1;
            }

            return Math.Max(leftDepth, rightDepth) + 1;
        }
    }
}