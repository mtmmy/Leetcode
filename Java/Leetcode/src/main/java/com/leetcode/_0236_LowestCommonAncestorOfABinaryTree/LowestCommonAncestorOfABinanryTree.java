package com.leetcode._0236_LowestCommonAncestorOfABinaryTree;

import com.leetcode.utils.TreeNode;

public class LowestCommonAncestorOfABinanryTree {
    public TreeNode solution(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root.val == p.val || root.val == q.val) {
            return root;
        }
        TreeNode left = solution(root.left, p, q);
        TreeNode right = solution(root.right, p, q);

        if (left != null && right != null) {
            return root;
        }
        return left == null ? right : left;
    }
}
