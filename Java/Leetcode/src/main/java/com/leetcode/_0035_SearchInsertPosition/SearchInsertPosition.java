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
    public int SearchInsert(int[] nums, int target) {
        
        for (int i=0; i<nums.length; i++) {
            if (nums[i] >= target) {
                return i;
            }
        }        
        return nums.length;
    }
}
