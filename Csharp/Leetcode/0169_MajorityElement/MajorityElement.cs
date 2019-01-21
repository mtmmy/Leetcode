using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class MajorityElement {
        public int Solution(int[] nums) {

            var dictionary = new Dictionary<int, int>();
            var halfLength = nums.Length / 2;

            for (int i = 0; i < nums.Length; i++) {
                var num = nums[i];
                if (dictionary.ContainsKey(num)) {
                    dictionary[num]++;
                } else {
                    dictionary.Add(num, 1);
                }
                if (dictionary[num] > halfLength) {
                    return num;
                }
            }
            return -1;
        }

        // Moore voting algorithm
        public int Solution2(int[] nums) {            
            int major = nums[0];
            int count = 1;
            
            for (int i = 1; i < nums.Length; i++) {
                if (nums[i] == major) {
                    count++;
                } else if (--count == 0) {
                    major = nums[i];
                    count = 1;
                }
            }
            
            return major;
        }
    }
}