package com.leetcode._0364_NestedListWeightSum2;

import com.leetcode._0341_FlattenNestedListIterator.NestedInteger;

import java.util.ArrayList;
import java.util.List;

public class NestedListWeightSum2 {
    public int depthSumInverse(List<NestedInteger> nestedList) {
        List<Integer> layerSum = new ArrayList<>();

        for (NestedInteger ni : nestedList) {
            dfs(ni, layerSum, 0);
        }

        int result = 0;
        for (int i = 0; i < layerSum.size(); i++) {
            result += (layerSum.size() - i) * layerSum.get(i);
        }
        return result;
    }

    public void dfs(NestedInteger nestedInteger, List<Integer> layerSum, int depth) {

        if (depth >= layerSum.size()) {
            layerSum.add(0);
        }
        if (nestedInteger.isInteger()) {
            int val = nestedInteger.getInteger();
            layerSum.set(depth, layerSum.get(depth) + val);
        } else {
            for (NestedInteger ni : nestedInteger.getList()) {
                dfs(ni, layerSum, depth + 1);
            }
        }
    }
}
