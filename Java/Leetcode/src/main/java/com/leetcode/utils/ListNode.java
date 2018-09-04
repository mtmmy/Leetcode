package com.leetcode.utils;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode() {}
    public ListNode(int x) { val = x; }

    @Override
    public String toString() {
        String result = "";
        ListNode curNode = this;

        while(curNode != null) {

            result += String.valueOf(curNode.val);

            if (curNode.next != null) {
                result += ", ";
            }

            curNode = curNode.next;
        }

        return result;
    }
}
