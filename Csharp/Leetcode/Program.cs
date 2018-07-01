using System;
using System.Collections.Generic;
using System.Linq;
using Leetcode.Solutions;
using Leetcode.Utils;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

            var toolKit = new ToolKit();
            var target = new TwoSum2_InputArrayIsSorted();

            var result = target.Solution(new int[] {2, 3, 4}, 6);
            Console.WriteLine(result);

        }
    }
}
