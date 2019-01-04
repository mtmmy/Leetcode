using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class MinimumDepthOfBinaryTree {
        public int MinDepth(TreeNode root) {
            if (root == null) {
                return 0;
            }

            var leftDepth = MinDepth(root.left);
            var rightDepth = MinDepth(root.right);

            if (leftDepth != 0 && rightDepth != 0) {
                return Math.Min(leftDepth, rightDepth) + 1;
            } else {
                return Math.Max(leftDepth, rightDepth) + 1;
            }
        }
    }
}
