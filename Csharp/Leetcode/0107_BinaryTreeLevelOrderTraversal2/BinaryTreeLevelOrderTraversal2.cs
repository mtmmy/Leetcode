using System;
using System.Collections.Generic;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class BinaryTreeLevelOrderTraversal2 {
        public IList<IList<int>> LevelOrderBottom(TreeNode root) {
            var result = new List<IList<int>>();

            // DFS solution
            var queue = new Queue<TreeNode>();

            if (root == null) {
                return result;
            }
            queue.Enqueue(root);
            while (queue.Count > 0) {
                var nodesCountInLevel = queue.Count;
                var subList = new List<int>();
                for (int i = 0; i < nodesCountInLevel; i++) {
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
    }
}


//======
/* 
    //======
        #107 Binary Tree Level Order Traversal II
    //======
        Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

        For example:
        Given binary tree [3,9,20,null,null,15,7],
        //example
            3
           / \
          9  20
            /  \
           15   7
        //example
        return its bottom-up level order traversal as:
        //example
        [
          [15,7],
          [9,20],
          [3]
        ]
        //example
    //======
        We use DFS. First we put the root node into a queue and create a loop which runs until the queue is empty.
        Inside the loop we have another loop that runs same amount of times of the length of queue. And we need to keep this value becaase in the loop we will add nodes into the queue.
        For example, at the beginning there is only the root node in the queue, this inner loop is executed once. 
        In the inner loop, we dequeue each node and store the value of the node to a temporary list and add its child into the queue.
        After the execution of the inner loop, we insert the temporary list to the beginning place of the result list.
        If there are no nodes in the queue, the programm ends and returns the result. Otherwise the programm keeps running.
    //======
        Tree, DFS
    //======
        05/13/2018
    //======
        Leetcode
    //======
        https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
    //======
*/