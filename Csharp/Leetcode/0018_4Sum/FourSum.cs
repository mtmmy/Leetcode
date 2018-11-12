using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class FourSum {
        Array.Sort(nums);
        var length3 = nums.Length - 3;
        var length2 = nums.Length - 2;
        
        for (var j = 0; j < nums.Length; j++) {
            if (j != 0 && nums[j] == nums[j - 1]) {
                continue;
            }
            int left = j + 1, right = nums.Length - 1;
            while (left < right) {
                var sum = nums[left] + nums[right];
                if (sum == -nums[j]) {
                    result.Add(new int[]{nums[j], nums[left], nums[right]});
                    do {
                        left++;
                    } while (left < right && nums[left] == nums[left - 1]);                    
                    do {
                        right--;   
                    } while (left < right && nums[right] == nums[right + 1]);
                } else if (sum > -nums[j]) {
                    right--;
                } else {
                    left++;
                }
            }
        }        
        return result;
    }
}
