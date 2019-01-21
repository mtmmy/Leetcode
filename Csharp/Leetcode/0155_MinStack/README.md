# [155. Min Stack](https://leetcode.com/problems/min-stack)

## Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

Example:

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

## Solution

We use a trick which is store the previous minimum number at the second place from the top of the stack. Hence when we pop the current minimum number, we can easily find the previous minimum number. We also use a varible to track the current min number.

For example we push -2 first, the stack will be as follows:

```
[MaxValue, -2]; min = -2
```
and then push 0:

```
[MaxValue, -2, 0]; min = -2
```
and then -3:

```
[MaxValue, -2, 0, -2, -3]; min = -3
```
When getMin() is called, we just return the variable **min**.

call pop():

```
[MaxValue, -2, 0]; min = -2
```
call top():

```
return 0
[MaxValue, -2, 0]; min = -2
```

Time complexiy: O(1) for every function

## Related Topics

[Stack](https://leetcode.com/tag/stack/) , [Design](https://leetcode.com/tag/design/) 

## Similar Questions

[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/), [Max Stack](https://leetcode.com/problems/max-stack/)
