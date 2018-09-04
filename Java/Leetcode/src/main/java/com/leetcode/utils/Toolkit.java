package com.leetcode.utils;


import java.util.Deque;
import java.util.LinkedList;

public class Toolkit {

    public ListNode GenerateListNode(int[] nums) {
        if (nums.length == 0) {
            return null;
        }

        ListNode curNode = new ListNode();
        ListNode head = curNode;
        for (int i = 0; i < nums.length; i++) {
            curNode.val = nums[i];

            if (i != nums.length - 1) {
                curNode.next = new ListNode();
                curNode = curNode.next;
            }
        }
        return head;
    }

    /// <summary>
    /// Take a string list and return the root of a binary tree.
    /// </summary>
    /// <returns>The tree node.</returns>
    /// <param name="vals">String list that contains numbers or the string "null."</param>
    public TreeNode GenerateTreeNode(String data) {
        data = data.replace("[", "").replace("]", "");

        if (data.isEmpty() || data.startsWith("null")) {
            return null;
        }

        String[] vals = data.split(",");

        int i = 0;
        TreeNode node2;
        TreeNode node1 = new TreeNode(Integer.valueOf(vals[i++]));
        Deque<TreeNode> queue = new LinkedList<>();
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
