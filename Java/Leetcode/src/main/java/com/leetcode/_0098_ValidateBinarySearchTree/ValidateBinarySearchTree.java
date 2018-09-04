package com.leetcode._0098_ValidateBinarySearchTree;
import com.leetcode.utils.TreeNode;

public class ValidateBinarySearchTree {
    public boolean solution(TreeNode root) {
        if (root == null) {
            return true;
        }
        return isValidSubBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean isValidSubBST(TreeNode root, long min, long max) {
        if (root == null) {
            return true;
        }
        if (root.val <= min || root.val >= max) {
            return false;
        }
        return isValidSubBST(root.left, min, root.val) && isValidSubBST(root.right, root.val, max);
    }
}
