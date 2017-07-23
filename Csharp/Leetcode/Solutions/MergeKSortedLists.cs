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

            int nodeListTrueLength = lists.Length;
            while (nodeListTrueLength > 1) {                
                for (int i=0; i<lists.Length; i++) {
                    //merge every two nodes
                    if (2*i+1 < lists.Length) {
                        //in order to simplify code, I call MergeTwoLists from another class
                        lists[i] = mergeTwo.MergeTwoLists(lists[2 * i], lists[2 * i + 1]);                        
                    } else if (2*i+1 == lists.Length) {                        
                        lists[i] = lists[2 * i];
                    }
                }
                nodeListTrueLength = (nodeListTrueLength + (nodeListTrueLength % 2 == 1 ? 1 : 0)) / 2;
                Array.Resize<ListNode>(ref lists, nodeListTrueLength);
            }

            return lists[0];
        }
    }
}
