﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Leetcode.Tools;

namespace Leetcode.Solutions {
    public class AddTwoNumbers {
        public ListNode AddTwoNumbersSolution(ListNode l1, ListNode l2) {
            var result = new ListNode(-1);
            var count = result;
            double carry = 0;

            while (l1 != null || l2 != null || carry > 0) {

                int value = (l1 != null && l1.val > 0 ? l1.val : 0) + (l2 != null && l2.val > 0 ? l2.val : 0) + (int)carry;
                carry = value / 10;
                carry = Math.Floor(carry);
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
