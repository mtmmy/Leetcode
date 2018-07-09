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
                if (a == null && b == null) {
                    return null;
                }

                if (a == null) {
                    a = headB;
                    b = b.next;
                } else if (b == null) {
                    b = headA;
                    a = a.next;
                } else {
                    a = a.next;
                    b = b.next;
                }
            }
            return a;
        }
    }
}

//======
/* 
    //======
160. Intersection of Two Linked Lists
    //======
   Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
    //======
        First, reverse the character arrays so that they can align on the first place which makes us easier to sum up digit by digit.
        Sum up two numbers digit by digit and remember carry over to the next place if there is a carryover.
        Reverse back to the correct number.

        We need character arrays to store reversed numbers, so the space complexity is O(n).
        We use a loop to sum up two numbers bit by bit, and the executing time of the loop depends on the longer number. The time complexity is O(n).
        And we also have 3 reversing steps. The time complexity of resersing is O(n) as well.
        So the total time complexity is still O(n).
    //======
        Linked List
    //======
        06/28/2018
    //======
        Leetcode
    //======
        https://leetcode.com/problems/intersection-of-two-linked-lists/description/
    //======
*/