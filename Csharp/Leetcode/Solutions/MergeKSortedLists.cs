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

            var nodeList = new List<ListNode>();
            for (int i=0; i<lists.Length; i++) {
                nodeList.Add(lists[i]);
            }

            int nodeListTrueLength = nodeList.Count;
            while (nodeListTrueLength > 1) {                
                for (int i=0; i<nodeList.Count; i++) {
                    //merge every two nodes
                    if (2*i+1 < nodeList.Count) {
                        //in order to simplify code, I call MergeTwoLists from another class
                        nodeList[i] = mergeTwo.MergeTwoLists(nodeList[2 * i], nodeList[2 * i + 1]);                        
                    } else if (2*i+1 == nodeList.Count) {                        
                        nodeList[i] = nodeList[2 * i];
                    }
                }
                if (nodeListTrueLength % 2 == 1) {
                    nodeListTrueLength = (nodeListTrueLength + 1) / 2;
                } else {
                    nodeListTrueLength /= 2;
                }
                for (int i=nodeListTrueLength; i<nodeList.Count; i++) {
                    nodeList[i] = null;
                }
            }

            return nodeList[0];
        }
    }
}
