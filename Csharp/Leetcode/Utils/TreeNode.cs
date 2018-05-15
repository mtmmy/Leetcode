using System;
using System.Collections.Generic;
using System.Linq;
namespace Leetcode.Utils {
    public class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode() {}
        public TreeNode(int x) { val = x; }

        public override string ToString() {
            var sList = new List<string>();
            var queue = new Queue<TreeNode>();
            queue.Enqueue(this);

            var nullCount = 0;
            while (queue.Count > 0) {
                var node = queue.Dequeue();

                if (node == null) {
                    nullCount++;
                } else {
                    if (nullCount > 0) {
                        for (int i = 0; i < nullCount; i++) {
                            sList.Add("null");
                        }
                        nullCount = 0;
                    }            
                    sList.Add(node.val.ToString());
                    queue.Enqueue(node.left);
                    queue.Enqueue(node.right);
                }
            }

            return sList.Aggregate((i, j) => i + ", " + j);
        }
    }
}
