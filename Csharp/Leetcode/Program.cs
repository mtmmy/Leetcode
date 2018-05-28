using System;
using System.Collections.Generic;
using System.Linq;
using Leetcode.Solutions;
using Leetcode.Utils;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

            var toolKit = new ToolKit();
            var target = new PathSum();
            var tree1 = toolKit.GenerateTreeNode(new List<string> { "5", "4", "8", "11", "null", "13", "4", "7", "2", "null", "null", "null", "1" });

            var result = target.HasPathSum(tree1, 22);
            Console.WriteLine();
            Console.WriteLine(result);
        }
    }
}
