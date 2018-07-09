using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class SingleNumber {
        public int FindSingleNumber(int[] nums) {
            
            //var container = new List<int>();
            //for (int i = 0; i < nums.Length; i++) {
            //    if (container.Contains(nums[i])) {
            //        container.Remove(nums[i]);
            //    } else {
            //        container.Add(nums[i]);
            //    }
            //}

            //return container[0];

            int result = 0;
            for (int i = 0; i < nums.Length; i++) {
                result ^= nums[i];
                Console.WriteLine(result);
            }
            return result;
        }
    }
}
