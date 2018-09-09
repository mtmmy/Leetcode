package com.leetcode;

import com.leetcode._0103_BinaryTreeZigzagLevelOrderTraversal.ZigzagLevelOrder;
import com.leetcode._0114_FlattenBinaryTreeToLinkedList.FlattenBinaryTreeToLinkedList;
import com.leetcode._0143_ReorderList.ReorderList;
import com.leetcode.utils.ListNode;
import com.leetcode.utils.Toolkit;
import com.leetcode.utils.TreeNode;


public class Application {
    
    public static void main(String[] args) {

        Toolkit toolkit = new Toolkit();

        TreeNode tree = toolkit.GenerateTreeNode("1,2,5,3,4,null,6");
        FlattenBinaryTreeToLinkedList target = new FlattenBinaryTreeToLinkedList();
        target.solution(tree);

        System.out.println("");
    }
}
