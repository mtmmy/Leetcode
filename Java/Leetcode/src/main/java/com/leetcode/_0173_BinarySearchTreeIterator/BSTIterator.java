package com.leetcode._0173_BinarySearchTreeIterator;

import com.leetcode.utils.TreeNode;

import java.util.Deque;
import java.util.LinkedList;

public class BSTIterator {
    Deque<TreeNode> stack;
    public BSTIterator(TreeNode root) {
        stack = new LinkedList<>();
        TreeNode curNode = root;
        while (curNode != null) {
            stack.push(curNode);
            curNode = curNode.left;
        }
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode top = stack.pop();

        TreeNode curNode = top.right;
        while (curNode != null) {
            stack.push(curNode);
            curNode = curNode.left;
        }

        return top.val;
    }
}
