using System;
using System.Collections.Generic;
using System.Linq;
using Leetcode.Solutions;
using Leetcode.Utils;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

            var toolKit = new ToolKit();
            var target = new LinkedListCycle();
            var node1 = new ListNode(0);
            var node2 = new ListNode(1);
            var node3 = new ListNode(2);
            var node4 = new ListNode(3);
            var node5 = new ListNode(4);

            node1.next = node2;
            node2.next = node3;
            node3.next = node4;
            node4.next = node5;
            node5.next = node1;


            Console.WriteLine(target.HasCycle(node1));
        }
    }
}
