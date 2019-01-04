using System;
using System.Linq;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class ConvertSortedArrayToBinarySearchTree {
        public TreeNode SortedArrayToBST(int[] nums) {
            return CreateBST(nums, 0, nums.Length - 1);
        }

        private TreeNode CreateBST(int[] nums, int low, int high) {
            if (low > high) {
                return null;
            }

            int mid = (low + high + 1) / 2;
            var cur = new TreeNode(nums[mid]);
            cur.left = CreateBST(nums, low, mid - 1);
            cur.right = CreateBST(nums, mid + 1, high);

            return cur;
        }
    }
}
