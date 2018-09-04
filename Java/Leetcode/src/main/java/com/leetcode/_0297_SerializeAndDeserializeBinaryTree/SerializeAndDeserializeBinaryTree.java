package com.leetcode._0297_SerializeAndDeserializeBinaryTree;

import com.leetcode.utils.TreeNode;

import java.util.*;

public class SerializeAndDeserializeBinaryTree {
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
        }
        List<String> sList = new ArrayList<>();
        Deque<TreeNode> queue = new LinkedList<>();
        queue.add(root);

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

        return String.join(",", sList);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {

        if (data.isEmpty() || data.startsWith("null")) {
            return null;
        }

        String[] vals = data.split(",");

        int i = 0;
        TreeNode node2;
        TreeNode node1 = new TreeNode(Integer.valueOf(vals[i++]));
        Deque<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(node1);
        TreeNode root = node1;

        while (queue.size() > 0) {
            node1 = queue.remove();
            if (i < vals.length) {
                String val = vals[i++];
                if (!val.equals("null")) {
                    node2 = new TreeNode(Integer.valueOf(val));
                    queue.add(node2);
                    node1.left = node2;
                }
            }

            if (i < vals.length) {
                String val = vals[i++];
                if (!val.equals("null")) {
                    node2 = new TreeNode(Integer.valueOf(val));
                    queue.add(node2);
                    node1.right = node2;
                }
            }
        }

        return root;
    }
}
