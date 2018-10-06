using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public IList<IList<int>> ThreeSum(int[] nums) {
        IList<IList<int>> result = new List<IList<int>>();
        Array.Sort(nums);
        
        for (var i = 0; i < nums.Length; i++) {
            if (i != 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1, right = nums.Length - 1;
            while (left < right) {
                var sum = nums[left] + nums[right];
                if (sum == -nums[i]) {
                    result.Add(new int[]{nums[i], nums[left], nums[right]});
                    do {
                        left++;
                    } while (left < right && nums[left] == nums[left - 1]);                    
                    do {
                        right--;   
                    } while (left < right && nums[right] == nums[right + 1]);
                } else if (sum > -nums[i]) {
                    right--;
                } else {
                    left++;
                }
            }
        }        
        return result;
    }
}
