package com.leetcode;

import com.leetcode._0103_BinaryTreeZigzagLevelOrderTraversal.ZigzagLevelOrder;
import com.leetcode._0114_FlattenBinaryTreeToLinkedList.FlattenBinaryTreeToLinkedList;
import com.leetcode._0143_ReorderList.ReorderList;
import com.leetcode._0272_ClosestBinarySearchTreeValue2.ClosestBinarySearchTreeValue2;
import com.leetcode._0445_AddTwoNumbers2.AddTwoNumber2;
import com.leetcode._0642_DesignSearchAutocompleteSystem.AutocompleteSystem;
import com.leetcode._0759_EmployeeFreeTime.EmployeeFreeTime;
import com.leetcode.utils.Interval;
import com.leetcode.utils.ListNode;
import com.leetcode.utils.Toolkit;
import com.leetcode.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Application {
    
    public static void main(String[] args) {

        Toolkit toolkit = new Toolkit();
//
        TreeNode tree = toolkit.GenerateTreeNode("4,2,5,1,3");
        ClosestBinarySearchTreeValue2 target = new ClosestBinarySearchTreeValue2();
        target.solution(tree, 3.714286, 2);

//        [4,2,5,1,3]
//        3.714286
//        2
    }
}
