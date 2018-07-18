package com.leetcode._0034_FindFirstAndLastPositionOfElementInSortedArray;

public class SearchForARange {
    public int[] searchRange(int[] nums, int target) {
     
        int[] result = new int[]{-1, -1};
        if (nums.length == 0) {
            return result;
        }        
        
        int begin = 0;
        int end = nums.length - 1;
        int mid = -1;        
        
        while(begin < end) {
            mid = (begin + end) / 2;
            
            if (target > nums[mid]) {
                begin = mid + 1;
            } else {
                end = mid;
            }
        }
        
        if (nums[begin] != target) {
            return result;
        }
        
        result[0] = begin;
        end = nums.length - 1;
        while(begin < end) {
            mid = (begin + end) / 2 + 1;
            if (nums[mid] > target) {
                end = mid - 1;
            } else {
                begin = mid;
            }
        }
        result[1] = end;
        
        
//        int i = 0;
//        int j = nums.length - 1;
//        
//        while(i < nums.length && j >= 0 && (nums[i] < target || nums[j] > target)) {
//            if (nums[i] < target) {
//                i++;
//            }
//            if (nums[j] > target) {
//                j--;
//            }
//        }        
//        
//        if (i < nums.length && j >= 0 && nums[i] <= nums[j]) {
//            result = new int[]{i, j};
//        }
        
        return result;
    }
}
