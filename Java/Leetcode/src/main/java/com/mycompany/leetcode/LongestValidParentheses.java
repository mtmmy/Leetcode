package com.mycompany.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LongestValidParentheses {

    public int longestValidParentheses(String s) {

        int longest = 0;
        List<Integer> dp = new ArrayList<>(Collections.nCopies(s.length() + 1, 0));

        for (int i = 1; i <= s.length(); i++) {
            int j = i - 2 - dp.get(i - 1);
            if (s.charAt(i - 1) == '(' || j < 0 || s.charAt(j) == ')') {
                dp.set(i, 0);
            } else {
                dp.set(i, dp.get(i - 1) + 2 + dp.get(j));
                longest = Math.max(longest, dp.get(i));
            }
        }

        return longest;
    }
}
