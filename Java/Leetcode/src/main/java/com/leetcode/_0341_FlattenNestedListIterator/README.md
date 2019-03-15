# [341. Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator)

## Description

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

```
Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
```

Example 2:

```
Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
```

## Solution

We first go through the root list in reversed way and put each element into a stack. Onec **hasNext()** is called, we check the size of the stack first. If it's not empty, we then peek the top element. If the element is integer, simply return **true**. Otherwise the element is a list, we break down it and push each element in it into the stack and keep running the while loop. For the **next()** function, we simply return the top element in the stack.

```
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
```

## Related Topics

[Stack](https://leetcode.com/tag/stack/) , [Design](https://leetcode.com/tag/design/) 

## Similar Questions

[Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/), [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/), [Mini Parser](https://leetcode.com/problems/mini-parser/), [Array Nesting](https://leetcode.com/problems/array-nesting/)
