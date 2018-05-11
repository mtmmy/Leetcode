using System;
using System.Collections.Generic;
using System.Linq;
using Leetcode.Solutions;
using Leetcode.Tools;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

			ThreeSum target = new ThreeSum();
            int[] nums = new int[] { -1, 0, 1, 2, -1, -4 };
            var expected = new List<List<int>>();
            expected.Add(new List<int> { -1, -1, 2 });
            expected.Add(new List<int> { -1, 0, 1 });

			var result = target.ThreeSumSolution(nums);

			var isEqual = result.SequenceEqual(expected);


			var test1 = new List<int> { 1, 2, 3 };
			var test2 = new List<int> { 1, 2, 3 };

			isEqual = test1.SequenceEqual(test2);

			Console.WriteLine("end");
        }
    }
}
