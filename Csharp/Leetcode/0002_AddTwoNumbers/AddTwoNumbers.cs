using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class AddTwoNumbers {
        public ListNode AddTwoNumbersSolution(ListNode l1, ListNode l2) {
            var result = new ListNode(-1);
	        var count = result;
	        int carry = 0;
	        
	        while (l1 != null || l2 != null || carry > 0) {
	            
	            int value = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) + carry;
	            carry = value / 10;
	            value = value % 10;
	            
	            count.next = new ListNode(value);
	            count = count.next;
	            
	            l1 = l1 == null ? null : l1.next;
	            l2 = l2 == null ? null : l2.next;
	        }
	        return result.next;
        }
    }
}

//======
/* 
    //======
        #2 Add Two Numbers
    //======
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Example

        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
    //======
        We use a loop to go through 2 linked lists and sum them up node by node. If there is a carryover, we store it and add it when the loop executes next time.
        At the end of a single execution of the loop, we need to check if the next node is null or not for both linked lists.
        The loop keeps executing until both linked list reach to the end and no carryover exits.

        The executing times depends on the length of the longer linked list. So the time complexity is O(n).
        And we need extra space to store the result, which makes the space complexity O(n) as well.
    //======
        Linked List
    //======
        04/01/2018
    //======
        Leetcode
    //======
        https://leetcode.com/problems/add-two-numbers/description/
    //======
*/