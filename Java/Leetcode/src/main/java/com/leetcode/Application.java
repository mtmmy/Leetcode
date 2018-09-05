package com.leetcode;

import com.leetcode._0103_BinaryTreeZigzagLevelOrderTraversal.ZigzagLevelOrder;
import com.leetcode.utils.Toolkit;
import com.leetcode.utils.TreeNode;


public class Application {
    
    public static void main(String[] args) {

        Toolkit toolkit = new Toolkit();
        TreeNode node = toolkit.GenerateTreeNode("3,9,20,6,13,15,7");
        ZigzagLevelOrder target = new ZigzagLevelOrder();
        target.zigzagLevelOrder(node);
        System.out.println("");
    }
}
