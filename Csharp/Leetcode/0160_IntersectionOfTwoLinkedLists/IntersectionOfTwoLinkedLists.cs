using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class IntersectionOfTwoLinkedLists {

        public ListNode Solution(ListNode headA, ListNode headB) {
            if (headA == null || headB == null) {
                return null;
            }

            int lengthA = GetLinkedListLength(headA);
            int lengthB = GetLinkedListLength(headB);

            if (lengthA > lengthB) {
                for (int i = 0; i < lengthA - lengthB; i++) {
                    headA = headA.next;
                }
            } else {
                for (int i = 0; i < lengthB - lengthA; i++) {
                    headB = headB.next;
                }
            }

            while (headA != null && headB != null) {
                if (ReferenceEquals(headA, headB)) {
                    return headA;
                }
                headA = headA.next;
                headB = headB.next;
            }
            return null;
        }

        private int GetLinkedListLength(ListNode node) {
            int count = 0;

            while (node != null) {
                count++;
                node = node.next;
            }

            return count;
        }

        public ListNode Solution2(ListNode headA, ListNode headB) {
            if (headA == null || headB == null) {
                return null;
            }

            var a = headA;
            var b = headB;

            while (!ReferenceEquals(a, b)) {            
                a = (a == null) ? headB : a.next;
                b = (b == null) ? headA : b.next;
            }
            
            return a;
        }
    }
}