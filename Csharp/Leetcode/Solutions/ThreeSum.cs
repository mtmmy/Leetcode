using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class ThreeSum {
        List<List<int>> result = new List<List<int>>();
        public List<List<int>> ThreeSumSolution(int[] nums) {

            Array.Sort(nums);
            for (var i = 0; i < nums.Length; i++) {
                if (i != 0 && nums[i] == nums[i - 1]) {
                    continue;
                }
                GetTwoSum(SubArray(nums, i + 1, nums.Length - i - 1), -nums[i]);
            }

            return result;
        }

        public void GetTwoSum(int[] nums, int target) {

            int i = 0, j = nums.Length - 1;
            while (i < j) {

                var sum = nums[i] + nums[j];
                if (sum == target) {
                    var tempList = new List<int>() { -target, nums[i], nums[j] };

                    if (result.Count > 0) {
                        var lastList = result[result.Count - 1];

                        if (tempList[0] != lastList[0] || tempList[1] != lastList[1] || tempList[1] != lastList[1]) {
                            result.Add(tempList);
                        }
                    } else {
                        result.Add(tempList);
                    }

                    i++;
                    j--;
                } else if (sum > target) {
                    j--;
                } else {
                    i++;
                }
            }
        }

        public int[] SubArray(int[] data, int index, int length) {
            int[] sub = new int[length];
            Array.Copy(data, index, sub, 0, length);
            return sub;
        }
    }
}
