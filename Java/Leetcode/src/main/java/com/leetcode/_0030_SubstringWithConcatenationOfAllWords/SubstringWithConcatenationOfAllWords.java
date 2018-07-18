/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.leetcode._0030_SubstringWithConcatenationOfAllWords;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 *
 * @author Hanmin Yang
 */
public class SubstringWithConcatenationOfAllWords {
    public List<Integer> findSubstring(String s, String[] words) {
        
        List<Integer> result = new ArrayList<>();
        if (words.length == 0 || s.isEmpty()) {
            return result;
        }
        
        Map<String, Integer> countTable1 = new HashMap<>();
        for (String w : words) {
            countTable1.put(w, countTable1.getOrDefault(w, 0) + 1);
        }
        
        int wordLength = words[0].length();
        int wordsTotalLength = wordLength * words.length;
        
        for (int i=0; i<=s.length() - wordsTotalLength; i++) {
        
            Map<String, Integer> countTable2 = new HashMap<>();
            int j = 0;
            for (j=0; j<words.length; j++) {
                String tempStr = s.substring(i + j * wordLength, i + j * wordLength + wordLength);
                if (!countTable1.containsKey(tempStr)) {
                    break;
                }
                countTable2.put(tempStr, countTable2.getOrDefault(tempStr, 0) + 1);
                if (countTable2.get(tempStr) > countTable1.get(tempStr)) {
                    break;
                }
            }
            if (j == words.length) {
                result.add(i);
            }
        }
        
        return result;
    }
}
