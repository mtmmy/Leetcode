using System;
namespace Leetcode.Solutions
{
    public class MaximumSubarray
    {
		public int MaxSubArray(int[] nums) {
			return MaxArray(nums, 0, nums.Length - 1);
		}

		private int MaxArray(int[] nums, int left, int right) {
            if (left == right) {
                return nums[left];
            }

            int middle = (left + right) / 2;
            var leftMax = MaxArray(nums, left, middle);
            var rightMax = MaxArray(nums, middle + 1, right);

			var middleSum = MiddleSum(nums, left, right, middle);

			return Math.Max(middleSum, Math.Max(leftMax, rightMax));
        }

		private int MiddleSum(int[] nums, int left, int right, int middle) {

			var leftSum = 0;
			var leftMax = nums[middle];
			for (int i = middle; i >= left; i--) {
				leftSum += nums[i];
				leftMax = Math.Max(leftMax, leftSum);
			}

			var rightSum = 0;
			var rightMax = nums[middle + 1];
			for (int i = middle + 1; i <= right; i++) {
				rightSum += nums[i];
				rightMax = Math.Max(rightMax, rightSum);
			}

			return Math.Max(rightMax + leftMax, Math.Max(rightMax, leftMax));
		}
    }
}
