using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class NextPermutation {
        public void NextPermutationSolution(int[] nums) {

            if (nums.Length < 2) {
                return;
            }

            int n = nums.Length;
            int j = n - 2;

            while (j >= 0 && nums[j] >= nums[j + 1]) {
                j--;
            }

            if (j < 0) {
                Reverse(nums);
                return;
            }

            int i = j + 1;
            while (i < n && nums[i] > nums[j]) {
                i++;
            }
            i--;

            Swap(ref nums[i], ref nums[j]);
            Array.Sort(nums, j + 1, nums.Length - j - 1);
        }

        private void Swap(ref int num1, ref int num2) {
            int temp = num1;
            num1 = num2;
            num2 = temp;
        }

        private void Reverse(int[] nums) {
            int half = nums.Length / 2;
            for (int i = 0; i < half; i++) {
                Swap(ref nums[i], ref nums[nums.Length - 1 - i]);
            }
        }
    }
}
