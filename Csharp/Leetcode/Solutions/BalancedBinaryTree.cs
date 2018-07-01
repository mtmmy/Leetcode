using System;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class BalancedBinaryTree {
        public bool IsBalanced(TreeNode root) {

            // O(n^2) solution
            //if (root == null) {
            //    return true;
            //}

            //var leftDepth = GetDepth(root.left);
            //var rightDepth = GetDepth(root.right);

            //return Math.Abs(leftDepth - rightDepth) <= 1 && IsBalanced(root.left) && IsBalanced(root.right);
            return DFSDepth(root) != -1;
        }

        private int GetDepth (TreeNode node) {
            if (node == null) {
                return 0;
            }
            return Math.Max(GetDepth(node.left), GetDepth(node.right)) + 1;
        }

        private int DFSDepth (TreeNode node) {
            if (node == null) {
                return 0;
            }

            var leftDepth = DFSDepth(node.left);
            if (leftDepth == -1) {
                return -1;
            }
            var rightDepth = DFSDepth(node.right);
            if (rightDepth == -1) {
                return -1;
            }

            if (Math.Abs(leftDepth - rightDepth) > 1) {
                return -1;
            }

            return Math.Max(leftDepth, rightDepth) + 1;
        }
    }
}

//======
/* 
    //======
        #110. Balanced Binary Tree
    //======
        Given a binary tree, determine if it is height-balanced.
        For this problem, a height-balanced binary tree is defined as:
        a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
    //======
        There are two kinds of solutions. 

        The first one is straitforward whose time complexity is O(n^2).
        We create a recursive function that can calculate the depth of a node, and we create another recursive function to check if chidren of each node are balanced.
        
        The second one only takes O(n).
        The idea of this solution is that we go through the tree with Deep First Search. When we reach the leaf nodes, they will return 1 which means the depth that count from themself to the bottom of the tree is 1.
        Every node will get the depth from its childre. We compare the depth of children of the node. If the differnce of two children is greater than 1, we return -1 to leave the recursive function.
        At the end of the program we only need to check if result equals to -1 or not.
        
    //======
        Tree, Recursive, DFS
    //======
        04/01/2018
    //======
        Leetcode
    //======
                https://leetcode.com/problems/balanced-binary-tree/description/
    //======
*/