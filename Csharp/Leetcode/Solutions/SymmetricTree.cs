using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class SymmetricTree {
        public bool IsSymmetric(TreeNode root) {
            return root == null || IsMirror(root.left, root.right);
        }

        private bool IsMirror(TreeNode left, TreeNode right) {

            if (left == null && right == null) {
                return true;
            }

            if (left == null || right == null) {
                return false;
            }

            return left.val == right.val && IsMirror(left.left, right.right) && IsMirror(left.right, right.left);
        }
    }
}
