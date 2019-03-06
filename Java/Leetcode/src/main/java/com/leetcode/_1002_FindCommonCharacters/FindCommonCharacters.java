package com.leetcode._1002_FindCommonCharacters;

import java.util.ArrayList;
import java.util.List;

public class FindCommonCharacters {
    public List<String> solution(String[] A) {
        int chars[] = new int[26];
        for (int i = 0; i < chars.length; i++) {
            chars[i] = 0;
        }
        for (int i = 0; i < A[0].length(); i++) {
            chars[A[0].charAt(i) - 'a']++;
        }

        for (String s : A) {
            int localChars[] = new int[26];
            for (int i = 0; i < localChars.length; i++) {
                localChars[i] = 0;
            }
            for (int i = 0; i < s.length(); i++) {
                localChars[s.charAt(i) - 'a']++;
            }
            for (int i = 0; i < 26; i++) {
                chars[i] = Math.min(chars[i], localChars[i]);
            }
        }

        List<String> result = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < chars[i]; j++) {
                result.add(Character.toString((char)('a' + i)));
            }
        }
        return result;
    }
}
