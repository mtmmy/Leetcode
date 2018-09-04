package com.leetcode._0341_FlattenNestedListIterator;

import java.util.Deque;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

// This program doesn't really work because there is no correct NestedInteger.
public class NestedIterator implements Iterator<Integer> {
    private Deque<NestedInteger> stack = new LinkedList<>();
    public NestedIterator(List<NestedInteger> nestedList) {
        for (int i = nestedList.size() - 1; i >= 0; i--) {
            stack.push(nestedList.get(i));
        }
    }

    @Override
    public Integer next() {
        return stack.pop().getInteger();
    }

    @Override
    public boolean hasNext() {
        while (!stack.isEmpty()) {
            NestedInteger top = stack.peek();
            if (top.isInteger()) {
                return true;
            }
            stack.pop();
            for (int i = top.getList().size() - 1; i >=0; i--) {
                stack.push(top.getList().get(i));
            }
        }
        return false;
    }
}

