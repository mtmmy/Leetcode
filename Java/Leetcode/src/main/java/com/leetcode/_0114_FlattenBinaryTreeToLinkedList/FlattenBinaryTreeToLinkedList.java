package com.leetcode._0114_FlattenBinaryTreeToLinkedList;

import com.leetcode.utils.TreeNode;

import java.util.Deque;
import java.util.LinkedList;

public class FlattenBinaryTreeToLinkedList {
    Deque<TreeNode> stack = new LinkedList<>();
    TreeNode rootNode = null;
    public void solution(TreeNode root) {
        dfs2(root);
        System.out.println("");
    }

    private void dfs2(TreeNode root) {
        if (root == null) {
            return;
        }
        dfs2(root.right);
        dfs2(root.left);
        root.right = rootNode;
        root.left = null;
        rootNode = root;
    }

    private void dfs(TreeNode root) {
        if (root == null) {
            return;
        }
        if (root.left != null) {
            if (root.right != null) {
                stack.addLast(root.right);
            }
            root.right = root.left;
            root.left = null;
        }
        dfs(root.right);
        if (!stack.isEmpty() && root.right == null) {
            root.right = stack.pollLast();
            dfs(root.right);
        }
    }
}
