package com.leetcode._0642_DesignSearchAutocompleteSystem;

import java.util.*;

public class AutocompleteSystem {

    Map<String, Integer> historicalData;
    String inputString;
    public AutocompleteSystem(String[] sentences, int[] times) {
        inputString = "";
        historicalData = new TreeMap<>();
        for (int i = 0; i < times.length; i++) {
            historicalData.put(sentences[i], times[i]);
        }
    }

    public List<String> input(char c) {
        if (c == '#') {
            historicalData.put(inputString, historicalData.getOrDefault(inputString, 0) + 1);
            inputString = "";
            return new ArrayList<>();
        }
        inputString += c;
        Map<Integer, List<String>> hottest = new TreeMap<>(Collections.reverseOrder());

        historicalData.entrySet().stream().forEach(e -> {
            String key = e.getKey();
            int val = e.getValue();

            if (key.startsWith(inputString)) {
                if (hottest.containsKey(val)) {
                    hottest.get(val).add(key);
                } else {
                    List<String> sentences = new ArrayList<>(Arrays.asList(key));
                    hottest.put(val, sentences);
                }
            }
        });

        List<String> result = new ArrayList<>();

        hottest.entrySet().stream().forEach(e -> {
            if (result.size() < 3 && e.getValue().size() <= 3 - result.size()) {
                result.addAll(e.getValue());
            } else {
                Collections.sort(e.getValue());
                for (String s : e.getValue()) {
                    if (result.size() < 3) {
                        result.add(s);
                    }
                }
            }
        });
        return result;
    }
}
