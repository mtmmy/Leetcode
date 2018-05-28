using System;
using System.Linq;
using Leetcode.Utils;

namespace Leetcode.Solutions {
    public class ConvertSortedArrayToBinarySearchTree {
        public TreeNode SortedArrayToBST(int[] nums) {
            return CreateBST(nums, 0, nums.Length - 1);
        }

        private TreeNode CreateBST(int[] nums, int left, int right) {

            if (left > right) {
                return null;
            }

            int mid = (left + right + 1) / 2;
            var root = new TreeNode(nums[mid]);
            root.left = CreateBST(nums, left, mid - 1);
            root.right = CreateBST(nums, mid + 1, right);

            return root;
        }
    }
}
