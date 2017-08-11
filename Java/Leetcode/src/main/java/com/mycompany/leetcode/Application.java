/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.leetcode;

import java.util.List;
import java.util.stream.Collectors;

/**
 *
 * @author Hanmin Yang
 */
public class Application {
    
    public static void main(String[] args) {

        SearchForARange target = new SearchForARange();
        int[] result = target.searchRange(new int[]{2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 8, 8, 9, 11}, 8);
        System.out.println("pause");
    }
}
