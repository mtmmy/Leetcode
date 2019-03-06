package com.leetcode._0340_LongestSubstringWithAtMostKDistinctCharacters;

import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithAtMostKDistinctCharacters {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int maxLen = 0, j = -1;
        Map<Character, Integer> charCount = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            int curCount = charCount.getOrDefault(cur, 0);
            charCount.put(cur, curCount + 1);

            while (charCount.size() > k) {
                char charJ = s.charAt(++j);
                int tempCount = charCount.get(charJ);
                charCount.put(charJ, tempCount - 1);
                if (tempCount - 1 == 0) {
                    charCount.remove(s.charAt(j));
                }
            }
            maxLen = Math.max(maxLen, i - j);
        }
        return maxLen;
    }
}
