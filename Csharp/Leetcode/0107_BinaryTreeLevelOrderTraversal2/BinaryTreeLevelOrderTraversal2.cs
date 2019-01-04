using System;
using System.Collections.Generic;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class BinaryTreeLevelOrderTraversal2 {
        public IList<IList<int>> LevelOrderBottom(TreeNode root) {
            var result = new List<IList<int>>();
            var queue = new Queue<TreeNode>();

            if (root == null) {
                return result;
            }
            queue.Enqueue(root);
            while (queue.Count > 0) {
                var levelNum = queue.Count;
                var subList = new List<int>();
                for (int i = 0; i < levelNum; i++) {
                    var node = queue.Dequeue();
                    if (node.left != null) {
                        queue.Enqueue(node.left);
                    }
                    if (node.right != null) {
                        queue.Enqueue(node.right);
                    }
                    subList.Add(node.val);
                }
                result.Add(subList);
            }

            result.Reverse();
            return result;
        }
    }
}