using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class LinkedListCycle {
        public bool HasCycle(ListNode head) {

            if (head == null) {
            return false;
        }


        var runOne = head;
        var runTwo = head;

        while (runTwo.next != null && runTwo.next.next != null) {
            runOne = runOne.next;
            runTwo = runTwo.next.next;
            if (ReferenceEquals(runOne, runTwo)) {
                return true;
            }
        }
        return false;
        }
    }
}
