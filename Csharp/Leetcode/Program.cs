using System;
using System.Collections.Generic;
using System.Linq;
using Leetcode.Solutions;
using Leetcode.Utils;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {
            
            var toolKit = new ToolKit();
            var target = new CombinationSum();
            var result = target.Solution(new int[] { 2, 3, 6, 7 }, 8);
            Console.WriteLine(result);
        }
    }
}
