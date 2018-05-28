using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class PathSum {
        public bool HasPathSum(TreeNode root, int sum) {
            return CompareSum(root, sum, 0);
        }

        private bool CompareSum(TreeNode root, int sum, int sumSoFar) {
            if (root == null) {
                return false;
            }

            var newSum = sumSoFar + root.val;
            if (root.left == null && root.right == null) {
                return sum == newSum;
            }

            var isLeftMatched = CompareSum(root.left, sum, newSum);
            var isRightMatched = CompareSum(root.right, sum, newSum);

            return isLeftMatched || isRightMatched;
        }
    }
}
