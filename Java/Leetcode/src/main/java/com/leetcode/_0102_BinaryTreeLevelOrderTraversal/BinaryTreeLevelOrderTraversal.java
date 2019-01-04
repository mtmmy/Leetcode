package com.leetcode._0102_BinaryTreeLevelOrderTraversal;

import com.leetcode.utils.TreeNode;

import java.util.*;

public class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> solution(TreeNode root) {

        List<List<Integer>> result = new ArrayList<>();        
        if (root == null) {
            return result;
        }
        Deque<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (queue.size() > 0) {
            int nodeCount = queue.size();

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
