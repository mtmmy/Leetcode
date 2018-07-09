using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class ThreeSumClosest {
        int minDiff = 9999999;

        public int ThreeSumClosestSolution(int[] nums, int target) {

            Array.Sort(nums);
            for (var i = 0; i < nums.Length; i++) {
                if (minDiff == 0) {
                    break;
                }
                if (i != 0 && nums[i] == nums[i - 1]) {
                    continue;
                }
                GetTwoSum(SubArray(nums, i + 1, nums.Length - i - 1), nums[i], target);
            }
            return target + minDiff;
        }

        public void GetTwoSum(int[] nums, int match3rd, int target) {

            int i = 0, j = nums.Length - 1;
            while (i < j) {

                var diff = nums[i] + nums[j] + match3rd - target;
                if (Math.Abs(diff) < Math.Abs(minDiff)) {
                    minDiff = diff;
                }

                if (diff == 0) {
                    return;
                } else if (diff >= 0) {
                    j--;
                } else {
                    i++;
                }
            }
        }

        public int[] SubArray(int[] data, int index, int length) {
            int[] result = new int[length];
            Array.Copy(data, index, result, 0, length);
            return result;
        }
    }
}
