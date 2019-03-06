package com.leetcode._0937_ReorderLogFiles;

import java.util.Arrays;

public class ReorderLogFiles {
    public String[] solution(String[] logs) {
        Arrays.sort(logs, (s1, s2) -> {
            String[] split1 = s1.split(" ", 2);
            String[] split2 = s2.split(" ", 2);
            boolean isWord1 = Character.isLetter(split1[1].charAt(0));
            boolean isWord2 = Character.isLetter(split2[1].charAt(0));

            if (isWord1 && isWord2) {
                int compare = split1[1].compareTo(split2[1]);
                if (compare == 0) {
                    return split1[0].compareTo(split2[0]);
                }
                return compare;
            }
            return isWord1 ? -1 : (isWord2 ? 1 : 0);
        });
        return logs;
    }
}
