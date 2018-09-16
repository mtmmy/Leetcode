package com.leetcode._0257_BinaryTreePaths;

import com.leetcode.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class BinaryTreePaths {
    public List<String> binaryTreePaths(TreeNode root) {

        List<String> result = new ArrayList<>();
        dfs(root, result, "");
        return result;
    }

    private void dfs (TreeNode node, List<String> result, String path) {
        if (node == null) {
            return;
        }
        path += String.valueOf(node.val);
        if (node.left == null && node.right == null) {
            result.add(path);
            return;
        }
        path += "->";

        dfs(node.left, result, path);
        dfs(node.right, result, path);
    }
}
