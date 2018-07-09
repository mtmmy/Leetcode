using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class TwoSum {

        public int[] TwoSumSolution(int[] nums, int target) {
            var map = new Dictionary<int, int>();

            for (var i = 0; i < nums.Length; i++) {
                int complement = target - nums[i];
                if (map.ContainsKey(complement)) {
                    return new int[] { map[complement], i };
                }
                map[nums[i]] = i;
            }
            return null;
        }
    }
}
