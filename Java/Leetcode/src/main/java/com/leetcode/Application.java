package com.leetcode;

import com.leetcode._0103_BinaryTreeZigzagLevelOrderTraversal.ZigzagLevelOrder;
import com.leetcode._0114_FlattenBinaryTreeToLinkedList.FlattenBinaryTreeToLinkedList;
import com.leetcode._0143_ReorderList.ReorderList;
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
//        TreeNode tree = toolkit.GenerateTreeNode("1,2,5,3,4,null,6");
//        FlattenBinaryTreeToLinkedList target = new FlattenBinaryTreeToLinkedList();
//        target.solution(tree);

        EmployeeFreeTime target = new EmployeeFreeTime();
        List<List<Interval>> schedule = new ArrayList<>();

        List<Interval> e1 = new ArrayList<Interval>() {{
            add(new Interval(1, 2));
            add(new Interval(5, 6));
        }};

        List<Interval> e2 = new ArrayList<Interval>() {{
            add(new Interval(1, 3));
        }};

        List<Interval> e3 = new ArrayList<Interval>() {{
            add(new Interval(4, 10));
        }};

        schedule.add(e1);
        schedule.add(e2);
        schedule.add(e3);

        target.solution(schedule);
    }
}
