/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.leetcode._0035_SearchInsertPosition;

/**
 *
 * @author Hanmin Yang
 */
public class SearchInsertPosition {
    public int solution(int[] nums, int target) {
        
        int begin = 0;
        int end = nums.length - 1;
        
        while (begin <= end) {
            int mid = (begin + end) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] > target) {
                end = mid - 1;
            } else {
                begin = mid + 1;
            }
        }
        return begin;
    }
}
