package com.leetcode._0103_BinaryTreeZigzagLevelOrderTraversal;

import com.leetcode.utils.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class ZigzagLevelOrder {

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {

        List<List<Integer>> result = new ArrayList<>();
        traverse(root, result, 0);
        return result;
    }

    private void traverse(TreeNode curNode, List<List<Integer>> result, int depth) {
        if (curNode == null) {
            return;
        }
        if (depth >= result.size()) {
            result.add(new LinkedList<>());
        }

        if (depth % 2 == 0) {
            result.get(depth).add(curNode.val);
        } else {
            result.get(depth).add(0, curNode.val);
        }
        traverse(curNode.left, result, depth + 1);
        traverse(curNode.right, result, depth + 1);
    }
}
