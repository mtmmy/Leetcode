package com.leetcode._0032_LongestValidParentheses;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LongestValidParentheses {

    public int solution(String s) {

        int longest = 0;
        int[] dp = new int[s.length() + 1];

        for (int i = 1; i <= s.length(); i++) {
            int j = i - 2 - dp[i-1];
            if (s.charAt(i - 1) == '(' || j < 0 || s.charAt(j) == ')') {
                dp[i] = 0;
            } else {
                dp[i] = dp[i-1] + 2 + dp[j];
                longest = Math.max(longest, dp[i]);
            }
        }

        return longest;
    }
}
