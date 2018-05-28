using System;
using System.Collections.Generic;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class BinaryTreeLevelOrderTraversal2 {
        public IList<IList<int>> LevelOrderBottom(TreeNode root) {
            var result = new List<IList<int>>();
            //if (root == null) {
            //    return result;
            //}

            //var queue = new Queue<TreeNode>();
            //queue.Enqueue(root);
            //queue.Enqueue(null);

            //result.Add(new List<int>());
            //while (queue.Count > 1) {
            //    var curNode = queue.Dequeue();
            //    if (curNode != null) {
            //        result[result.Count - 1].Add(curNode.val);
            //        if (curNode.left != null) {
            //            queue.Enqueue(curNode.left);
            //        }
            //        if (curNode.right != null) {
            //            queue.Enqueue(curNode.right);
            //        }
            //    } else {
            //        queue.Enqueue(null);
            //        result.Add(new List<int>());
            //    }
            //}

            //result.Reverse();

            // BFS solution
            //LevelMaker(result, root, 0);

            // DFS solution
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
                result.Insert(0, subList);
            }

            return result;
        }

        private void LevelMaker(List<IList<int>> list, TreeNode root, int level) {
            if (root == null) {
                return;
            }

            if (level >= list.Count) {
                list.Insert(0, new List<int>());
            }
            LevelMaker(list, root.left, level + 1);
            LevelMaker(list, root.right, level + 1);
            list[list.Count - level - 1].Add(root.val);
        }
    }
}

//public class Solution {
//    public List<List<Integer>> levelOrderBottom(TreeNode root) {
//        Queue<TreeNode> queue = new LinkedList<TreeNode>();
//        List<List<Integer>> wrapList = new LinkedList<List<Integer>>();

//        if (root == null) return wrapList;

//        queue.offer(root);
//        while (!queue.isEmpty()) {
//            int levelNum = queue.size();
//            List<Integer> subList = new LinkedList<Integer>();
//            for (int i = 0; i < levelNum; i++) {
//                if (queue.peek().left != null) queue.offer(queue.peek().left);
//                if (queue.peek().right != null) queue.offer(queue.peek().right);
//                subList.add(queue.poll().val);
//            }
//            wrapList.add(0, subList);
//        }
//        return wrapList;
//    }
//}