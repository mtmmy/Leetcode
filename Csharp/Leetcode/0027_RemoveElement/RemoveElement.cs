using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class RemoveElement {
        public int RemoveElementSolution(int[] nums, int val) {
            int begin = 0;
            for (int i = 0; i < nums.Length; i++) {
                if (nums[i] != val) {
                    nums[begin++] = nums[i];
                }
            }
            return begin;
        }
    }
}
