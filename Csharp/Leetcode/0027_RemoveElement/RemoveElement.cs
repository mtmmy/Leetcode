using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class RemoveElement {
        public int RemoveElementSolution(int[] nums, int val) {

            int i = 0;
            int j = nums.Length - 1;
            while (i <= j) {
                if (nums[i] == val && nums[j] != val) {
                    int temp = nums[i];
                    nums[i++] = nums[j];
                    nums[j--] = temp;
                }
                if (nums[i] != val) {
                    i++;
                }
                if (nums[j] == val) {
                    j--;
                }
            }

            return i;
        }

        public int RemoveElementSolutionAnother(int[] nums, int val) {

            int j = 0;
            for (int i = 0; i < nums.Length; i++) {
                if (nums[i] != val) {
                    nums[j++] = nums[i];
                }
            }
            return j;
        }
    }
}
