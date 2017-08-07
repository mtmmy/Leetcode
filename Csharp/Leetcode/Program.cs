using System;
using Leetcode.Solutions;
using Leetcode.Tools;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

            var obj = new NextPermutation();
            int[] nums = new int[] { 3, 2, 1, 3, 3, 1 };

            obj.NextPermutationSolution(nums);

            //Console.WriteLine(result);
            //Console.WriteLine("Leetcode problems!");
            Console.ReadLine();
        }
    }
}
