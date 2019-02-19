package com.leetcode._0272_ClosestBinarySearchTreeValue2;

import com.leetcode.utils.TreeNode;

import java.util.*;

public class ClosestBinarySearchTreeValue2 {

    public List<Integer> solution(TreeNode root, double target, int k) {
        Deque<Integer> queue = new ArrayDeque<Integer>();
        closestKValuesHelper(queue, root, target, k);
        return new ArrayList(queue);
    }
    
    private void closestKValuesHelper(Deque<Integer> queue, TreeNode root, double target, int k) {
        if (root == null) {
            return;
        }
        
        closestKValuesHelper(queue, root.left, target, k);
        
        if (queue.size() == k) {
            if (Math.abs(queue.getFirst() - target) < Math.abs(root.val - target)) {
                return;
            } else {
                queue.removeFirst();
            }
        }
        
        queue.addLast(root.val);
        closestKValuesHelper(queue, root.right, target, k);
    }

    private class ValDiff {
        public int val;
        public double diff;
        public ValDiff(int v, double d) { val = v; diff = d; }
    }

    public List<Integer> badSolution(TreeNode root, double target, int k) {
        List<Integer> result = new ArrayList<>();
        List<ValDiff> diffs = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        stack.addLast(root);

        while(!stack.isEmpty()) {
            TreeNode curNode = stack.pollLast();
            diffs.add(new ValDiff(curNode.val, Math.abs(target - curNode.val)));
            if (curNode.left != null) {
                stack.addLast(curNode.left);
            }
            if (curNode.right != null) {
                stack.addLast(curNode.right);
            }
        }

        Collections.sort(diffs, (d1, d2) -> {
            return d1.diff < d2.diff ? 1 : -1;
        });

        for (int i = 0; i < k; i++) {
            result.add(diffs.get(i).val);
        }
        return result;
    }
}
