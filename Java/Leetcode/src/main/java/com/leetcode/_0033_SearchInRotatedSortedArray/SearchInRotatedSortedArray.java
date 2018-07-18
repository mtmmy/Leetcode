package com.leetcode._0033_SearchInRotatedSortedArray;

public class SearchInRotatedSortedArray {

    public int search(int[] nums, int target) {

        int begin = 0;
        int end = nums.length - 1;
        
        while (begin < end) {
            int mid = (begin + end) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            
            if (nums[end] <= nums[mid]) {
                if (target >= nums[begin] && target < nums[mid]) {
                    end = mid - 1;
                } else {
                    begin = mid + 1;
                }
            } else {
                if (target > nums[mid] && target <= nums[end]) {
                    begin = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        return nums.length == 0 ? -1 : nums[begin] == target ? begin : -1;
    }
}
