using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Leetcode.Tools;

namespace Leetcode.Solutions {
    public class MergeKSortedLists {
        public ListNode MergeKLists(ListNode[] lists) {

            MergedTwoSortedList mergeTwo = new MergedTwoSortedList();
            if (lists.Length == 0) {
                return null;
            }
            
            while (lists.Length > 1) {
                //merge every two nodes
                var half = lists.Length / 2;
                for (int i=0; i<half; i++) {                    
                    //in order to simplify code, I call MergeTwoLists from another class
                    lists[i] = mergeTwo.MergeTwoLists(lists[2 * i], lists[2 * i + 1]);                    
                }
                if (lists.Length % 2 == 1) {
                    lists[lists.Length / 2] = lists[lists.Length - 1];
                }
                var nodeListTrueLength = (lists.Length + (lists.Length % 2 == 1 ? 1 : 0)) / 2;
                Array.Resize<ListNode>(ref lists, nodeListTrueLength);
            }

            return lists[0];
        }
    }
}
