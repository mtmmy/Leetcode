using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class MinStack {

        private int min = Int32.MaxValue;
        private Stack<int> stack;

        /** initialize your data structure here. */
        public MinStack() {
            stack = new Stack<int>();
        }

        public void Push(int x) {
            if (x <= min) {
                stack.Push(min);
                min = x;
            }
            stack.Push(x);
        }

        public void Pop() {
            int popOut = stack.Pop();

            if (popOut == min) {
                min = stack.Pop();
            }
        }

        public int Top() {
            return stack.Peek();
        }

        public int GetMin() {
            return min;
        }
    }
}

//======
/* 
    //======
155. Min Stack
    //======
   Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
    //======
        The real problem of this question is how to get the minimum value in the stack in constant time. 
        This means no matter how big the stack is, we can always get the minimum value in one step so that the time complexity of GetMin() is O(1).
        This also means we can not use a loop to find out the minimum value because the time complexit of this soultion is O(n).
        
        In order to find the minimum value in constant time, we need to keep it and update it when every time Push(int x) is called.
        However, the minimum number can be poped, we also need to keep the second minimum value. So when a new number is pushed into the stack, we compare it to the minumum value.
        If the new number isn't greater than the minimum number, we push the old minimum number into the queue before we pushed the new number. 
        The reason that we push the old minimum value is we can keep it as the second minimum value. Otherwise we simply push the new number.

        When we do pop we also need to check if the value that will be popped is the same as the minimum value. If so, we need to pop the second minimum number because it's just the indicator number which isn't a real element of the stack.
        Otherwise we just simply pop the number.
    //======
        Stack
    //======
        06/28/2018
    //======
        Leetcode
    //======
    https://leetcode.com/problems/min-stack/description/
    //======
*/