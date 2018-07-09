using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class FourSum {
        IList<IList<int>> result = new List<IList<int>>();
        public IList<IList<int>> FourSumSolution(int[] nums, int target) {
            Array.Sort(nums);
            if (nums.Length == 0) {
                return result;
            }

            for (var i = 0; i < nums.Length; i++) {
                if (i != 0 && nums[i] == nums[i - 1]) {
                    continue;
                }
                for (var j = i + 1; j < nums.Length; j++) {
                    if (j != i + 1 && nums[j] == nums[j - 1]) {
                        continue;
                    }
                    GetTwoSum(SubArray(nums, j + 1, nums.Length - j - 1), -nums[i], -nums[j], target);
                }
            }

            return result;
        }

        public void GetTwoSum(int[] nums, int num1, int num2, int target) {

            target += num1 + num2;
            int i = 0, j = nums.Length - 1;
            while (i < j) {

                var sum = nums[i] + nums[j];
                if (sum == target) {
                    var tempList = new List<int>() { -num1, -num2, nums[i], nums[j] };
                    if (result.Count > 0) {
                        var lastList = result[result.Count - 1];

                        if (tempList[0] != lastList[0] || tempList[1] != lastList[1] || tempList[2] != lastList[2]) {
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
            int[] result = new int[length];
            Array.Copy(data, index, result, 0, length);
            return result;
        }
    }
}
