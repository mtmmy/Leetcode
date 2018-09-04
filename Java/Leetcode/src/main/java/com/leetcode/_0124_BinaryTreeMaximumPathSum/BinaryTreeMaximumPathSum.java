package com.leetcode._0124_BinaryTreeMaximumPathSum;

import com.leetcode.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class BinaryTreeMaximumPathSum {
    int result = Integer.MIN_VALUE;
    public int solution(TreeNode root) {
        if (root == null) {
            return 0;
        }
        dfs(root);
        return result;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = Math.max(0, dfs(root.left));
        int right = Math.max(0, dfs(root.right));
        result = Math.max(result, left + right + root.val);
        return Math.max(left, right) + root.val;
    }
}
