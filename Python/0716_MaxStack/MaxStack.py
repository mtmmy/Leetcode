class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stackMax = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stackMax or self.stackMax[-1] <= x:
            self.stackMax.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        pop = self.stack.pop()
        if self.stackMax and pop == self.stackMax[-1]:
            self.stackMax.pop()
        return pop

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stackMax[-1]

    def popMax(self):
        """
        :rtype: int
        """
        maximum = self.stackMax.pop()
        stackTemp = []
        
        while self.stack[-1] != maximum:
            stackTemp.append(self.stack.pop())
        self.stack.pop()
        
        while stackTemp:
            self.push(stackTemp.pop())
        
        return maximum

if __name__ == '__main__':
    target = MaxStack()
    target.push(5)
    target.push(1)
    print(target.popMax())
    print(target.peekMax())