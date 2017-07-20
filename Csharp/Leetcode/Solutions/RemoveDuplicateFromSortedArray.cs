using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class RemoveDuplicateFromSortedArray {
        public int RemoveDuplicates(int[] nums) {

            if (nums.Length == 0) {
                return 0;
            }

            int end = 0;

            for (var i = 0; i < nums.Length; i++) {
                if (nums[i] != nums[end]) {
                    end++;
                    if (i != end) {
                        nums[end] = nums[i];
                    }
                }
            }
            return end + 1;
        }
    }
}
