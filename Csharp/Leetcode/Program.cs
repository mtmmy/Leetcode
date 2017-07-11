using System;

namespace Leetcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
			int[] testAry = { 2, 7, 11, 15 };
			int target = 9;
			int[] result = TwoSum.Solution(testAry, target);
			Console.WriteLine("[" + string.Join(",", result) + "]");
        }
    }
}
