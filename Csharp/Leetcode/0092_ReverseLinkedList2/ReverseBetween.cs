using System;
using Leetcode.Utils;
namespace Leetcode.Solutions {
    public class ReverseBetween {
        public ListNode Solution(ListNode head, int m, int n) {
            if (m < 1 || n < m || head == null) {
                return null;
            }


            var i = 1;
            ListNode portBegin = null;
            ListNode portEnd = null;
            var curNode = head;
            ListNode preNode = null;
            ListNode tempNode = null;
            ListNode startNode = null;

            while (curNode != null) {
                if (m != 1 && i + 1 == m) {
                    portBegin = curNode;   
                }

                if (i == m) {
                    startNode = curNode;
                }

                if (i == n) {
                    portEnd = curNode.next;
                }

                if (i >= m && i <= n) {
                    tempNode = curNode;
                    curNode = curNode.next;
                    tempNode.next = preNode;
                    preNode = tempNode;
                } else {
                    curNode = curNode.next;
                }

                i++;
            }

            if (i <= n) {
                return null;
            }

            startNode.next = portEnd;
            if (portBegin != null) {
                portBegin.next = tempNode;
                return head;
            }
            return tempNode;
        }

        private ListNode Reverse(ListNode head) {

            if (head == null) {
                return null;
            }

            var curNode = head;
            ListNode preNode = null;
            ListNode tempNode = null;

            while (curNode != null) {
                tempNode = curNode;
                curNode = curNode.next;
                tempNode.next = preNode;
                preNode = tempNode;
            }

            return tempNode;
        }
    }
}
