using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class MergeKSortedLists {
        public ListNode MergeKLists(ListNode[] lists) {

            MergedTwoSortedList mergeTwo = new MergedTwoSortedList();
            if (lists.Length == 0) {
                return null;
            }
            
            var listLength = lists.Length;
        
            while (listLength > 1) {
                //merge every two nodes
                for (int i=0; i<listLength/2; i++) {                    
                    //in order to simplify code, I call MergeTwoLists from another class
                    lists[i] = MergeTwoLists(lists[2 * i], lists[2 * i + 1]);                    
                }
                if (listLength % 2 == 1) {
                    lists[listLength / 2] = lists[listLength - 1];
                }
                listLength = (listLength + (listLength % 2 == 1 ? 1 : 0)) / 2;
            }

            return lists[0];
        }

        public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
            if (l1 == null) {
                return l2;
            }
            
            if (l2 == null) {
                return l1;
            }
            
            if (l1.val < l2. val) {
                l1.next = MergeTwoLists(l1.next, l2);
                return l1;
            } else {
                l2.next = MergeTwoLists(l1, l2.next);
                return l2;
            }

            //             ListNode head = null; ;
//             ListNode cur = null;

//             if (l1 == null && l2 == null) {
//                 return head;
//             }

//             if (l1 == null) {
//                 head = new ListNode(l2.val);
//                 l2 = l2.next;
//             } else if (l2 == null) {
//                 head = new ListNode(l1.val);
//                 l1 = l1.next;
//             } else if (l1.val <= l2.val) {
//                 head = new ListNode(l1.val);
//                 l1 = l1.next;
//             } else {
//                 head = new ListNode(l2.val);
//                 l2 = l2.next;
//             }
//             cur = head;

//             while (l1 != null || l2 != null) {

//                 if (l1 == null) {
//                     cur.next = l2;
//                     break;
//                 } else if (l2 == null) {
//                     cur.next = l1;
//                     break;
//                 } else if (l1.val <= l2.val) {
//                     cur.next = new ListNode(l1.val);
//                     l1 = l1.next;
//                 } else {
//                     cur.next = new ListNode(l2.val);
//                     l2 = l2.next;
//                 }
//                 cur = cur.next;
//             }
//             return head;
        }
    }
}
