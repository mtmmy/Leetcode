using System;
using Leetcode.Solutions;
using Leetcode.Tools;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

            MergeKSortedLists merge = new MergeKSortedLists();
            
            int size = 10;
            ListNode[] array = new ListNode[size];
            for (int i=0; i<size; i++) {
                var node = new ListNode(2 * i);
                node.next = new ListNode(2 * i + 1);
                array[i] = node;
            }

            var result = merge.MergeKLists(array);
            var cur = result;
            while (cur != null) {
                Console.Write(cur.val + ", ");
                cur = cur.next;
            }

            //Console.WriteLine("Leetcode problems!");
            Console.ReadLine();
        }
    }
}
