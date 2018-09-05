package com.leetcode._0543_DiameterOfBinaryTree;

import com.leetcode.utils.TreeNode;

public class DiameterOfBinaryTree {
    int max = 0;
    public int solution(TreeNode root) {
        maxDepth(root);
        return max;
    }

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        max = Math.max(max, left + right);

        return Math.max(left, right) + 1;
    }
}
