using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class LinkedListCycle {
        public bool HasCycle(ListNode head) {

            if (head == null || head.next == null) {
                return false;
            }


            var runOne = head;
            var runTwo = head.next;
            var count = 0;

            while (runOne != null && runTwo != null) {
                count++;
                if (ReferenceEquals(runOne, runTwo)) {
                    Console.WriteLine(count);
                    return true;
                }

                runOne = runOne.next;
                if (runTwo.next == null) {
                    break;
                }
                runTwo = runTwo.next.next;
            }
            Console.WriteLine(count);
            return false;
        }
    }
}
