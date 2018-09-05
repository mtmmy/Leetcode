package com.leetcode._0617_MergeTwoBinaryTrees;

import com.leetcode.utils.TreeNode;

public class MergeTwoBinaryTrees {
    public TreeNode solution(TreeNode t1, TreeNode t2) {

        if (t1 == null || t2 == null) return t1 == null ? t2 : t1;
        t1.val = t1.val + t2.val;
        t1.left = solution(t1.left, t2.left);
        t1.right = solution(t1.right, t2.right);
        return t1;
    }

    public TreeNode solution2(TreeNode t1, TreeNode t2) {
         if (t1 == null && t2 == null) {
             return null;
         }
         TreeNode newTree = new TreeNode(-1);
         mergeNodes(newTree, t1, t2);
         return newTree;
    }

     private TreeNode mergeNodes(TreeNode newTree, TreeNode t1, TreeNode t2) {
         newTree.left = null;
         newTree.right = null;
         if (t1 != null && t2 != null) {
             newTree.val = t1.val + t2.val;
             newTree.left = mergeNodes(new TreeNode(-1), t1.left, t2.left);
             newTree.right = mergeNodes(new TreeNode(-1), t1.right, t2.right);
         } else if (t1 != null) {
             newTree.val = t1.val;
             newTree.left = mergeNodes(new TreeNode(-1), t1.left, null);
             newTree.right = mergeNodes(new TreeNode(-1), t1.right, null);
         } else if (t2 != null) {
             newTree.val = t2.val;
             newTree.left = mergeNodes(new TreeNode(-1), null, t2.left);
             newTree.right = mergeNodes(new TreeNode(-1), null, t2.right);
         } else {
             newTree = null;
         }

         return newTree;
     }
}
