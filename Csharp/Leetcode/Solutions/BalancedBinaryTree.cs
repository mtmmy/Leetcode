using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class BalancedBinaryTree {
        public bool IsBalanced(TreeNode root) {

            // O(n^2) solution
            //if (root == null) {
            //    return true;
            //}

            //var leftDepth = GetDepth(root.left);
            //var rightDepth = GetDepth(root.right);

            //return Math.Abs(leftDepth - rightDepth) <= 1 && IsBalanced(root.left) && IsBalanced(root.right);
            return DFSDepth(root) != -1;
        }

        private int GetDepth (TreeNode node) {
            if (node == null) {
                return 0;
            }
            return Math.Max(GetDepth(node.left), GetDepth(node.right)) + 1;
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
