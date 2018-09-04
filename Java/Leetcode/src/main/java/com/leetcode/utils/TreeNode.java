package com.leetcode.utils;

import java.util.*;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }

    @Override
    public String toString() {
        List<String> sList = new ArrayList<>();
        Deque<TreeNode> queue = new LinkedList<>();
        queue.add(this);

        int nullCount = 0;
        while (queue.size() > 0) {
            TreeNode node = queue.remove();

            if (node == null) {
                nullCount++;
            } else {
                if (nullCount > 0) {
                    for (int i = 0; i < nullCount; i++) {
                        sList.add("null");
                    }
                    nullCount = 0;
                }
                sList.add(String.valueOf(node.val));
                queue.add(node.left);
                queue.add(node.right);
            }
        }

        return String.join(", ", sList);
    }
}
