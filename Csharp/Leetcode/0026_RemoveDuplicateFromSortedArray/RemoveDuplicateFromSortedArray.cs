using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class RemoveDuplicateFromSortedArray {
        public int RemoveDuplicates(int[] nums) {

            if (nums.Length <= 1) {
                return nums.Length;
            }
            
            int uniqueIdx = 0;
            
            for (int i = 1; i < nums.Length; i++) {
                if (nums[i] != nums[uniqueIdx]) {
                    uniqueIdx++;
                    if (i != uniqueIdx) {
                        nums[uniqueIdx] = nums[i];    
                    }
                }
            }
            return uniqueIdx + 1;
        }
    }
}
