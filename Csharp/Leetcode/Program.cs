using System;
using System.Collections.Generic;
using System.Linq;
using Leetcode.Solutions;
using Leetcode.Utils;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

            var toolKit = new ToolKit();
            var target = new SameTree();
            var tree1 = toolKit.GenerateTreeNode(new List<string> { "0", "null", "1", "null", "2", "null", "3", "5", "4" });
            var tree2 = toolKit.GenerateTreeNode(new List<string> { "0", "1", "2", "3", "null", "null", "4" });
            var s = tree1.ToString();
            var result = target.IsSameTree(tree1, tree1);

            toolKit.GenerateTreeNode(new List<string> { "0", "1", "2", "3", "null", "null", "4" });

			Console.WriteLine(result);
        }
    }
}
