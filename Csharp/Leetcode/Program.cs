using System;
using System.Collections.Generic;
using System.Linq;
using Leetcode.Solutions;
using Leetcode.Tools;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

            ListNode listNode = new ListNode(1);
            listNode.next = new ListNode(1);
            listNode.next.next = new ListNode(2);
            listNode.next.next.next = new ListNode(2);
            listNode.next.next.next.next = new ListNode(3);
            listNode.next.next.next.next.next = new ListNode(3);

            var test = new ListNode("1, 1, 2, , 3, 3");

            var target = new RemoveDuplicatesFromSortedList();
            var result = target.Solution(listNode);

            //while(result != null) {
            //    Console.WriteLine(result.val);
            //    result = result.next;
            //}

			Console.WriteLine(result);
        }
    }
}
