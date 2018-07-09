using System;
using System.Collections.Generic;
using System.Linq;
using Leetcode.Utils;
namespace Leetcode.Solutions {
    public class SameTree {
        public bool IsSameTree(TreeNode p, TreeNode q) {
            //var queueP = new Queue<TreeNode>();
            //var queueQ = new Queue<TreeNode>();

            //var valP = new List<string>();
            //var valQ = new List<string>();

            //queueP.Enqueue(p);

            //while (queueP.Count > 0) {
            //    var node = queueP.Dequeue();

            //    valP.Add(node == null ? "null" : node.val.ToString());

            //    if (node != null) {
            //        queueP.Enqueue(node.left);
            //        queueP.Enqueue(node.right);
            //    }
            //}

            //queueQ.Enqueue(q);
            //while (queueQ.Count > 0) {
            //    var node = queueQ.Dequeue();

            //    valQ.Add(node == null ? "null" : node.val.ToString());

            //    if (node != null) {
            //        queueQ.Enqueue(node.left);
            //        queueQ.Enqueue(node.right);
            //    }
            //}

            //var stringP = valP.Aggregate((i, j) => i + ", " + j);
            //var stringQ = valQ.Aggregate((i, j) => i + ", " + j);

            //return stringP == stringQ;

            if (p == null && q == null) {
                return true;
            }

            if (p == null || q == null) {
                return false;
            }

            return p.val == q.val && IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right);
        }
    }
}
