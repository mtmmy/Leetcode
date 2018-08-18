using System;
using System.Collections.Generic;
using Leetcode.Utils;
namespace Leetcode.Solutions {
    public class InorderTraversal {
        public IList<int> Solution(TreeNode root) {
            if (root == null) {
                return new List<int>();
            }

            IList<int> result = new List<int>();
            Stack<TreeNode> stack = new Stack<TreeNode>();
            var curNode = root;
            stack.Push(root);

            while (stack.Count != 0) {
                curNode = stack.Pop();
                if (curNode.left == null && curNode.right == null) {
                    result.Add(curNode.val);
                } else {
                    if (curNode.right != null) {
                        stack.Push(curNode.right);
                        if (curNode.left == null) {
                            stack.Push(curNode);
                        }
                        curNode.right = null;
                    }
                    if (curNode.left != null) {
                        stack.Push(curNode);
                        stack.Push(curNode.left);
                        curNode.left = null;
                    }
                }
            }

            return result;
        }
    }
}
