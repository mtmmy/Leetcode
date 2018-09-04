package com.leetcode._0102_BinaryTreeLevelOrderTraversal;

import com.leetcode.utils.TreeNode;

import java.util.*;

public class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> solution(TreeNode root) {

        Deque<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> result = new ArrayList<>();
        queue.add(root);

        while (true) {
            int nodeCount = queue.size();
            if (nodeCount == 0) {
                break;
            }

            List<Integer> level = new ArrayList<>();
            while (nodeCount > 0) {
                TreeNode curNode = queue.remove();
                level.add(curNode.val);
                if (curNode.left != null) {
                    queue.add(curNode.left);
                }
                if (curNode.right != null) {
                    queue.add(curNode.right);
                }
                nodeCount--;
            }
            result.add(level);
        }
        return result;
    }
}
