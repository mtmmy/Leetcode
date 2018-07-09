using System;
using System.Collections.Generic;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class MaximumDepthOfBinaryTree {
        public int MaxDepth(TreeNode root) {
            if (root == null) {
                return 0;
            }

            return Math.Max(MaxDepth(root.left), MaxDepth(root.right)) + 1;
        }
    }
}
