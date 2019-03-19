class Solution:
    def calculate(self, s: str) -> int:
        def operation(op, num2, num1):
            if op == "+":
                return num1 + num2
            if op == "-":
                return num1 - num2
            if op == "*":
                return num1 * num2
            if op == "/":
                return num1 // num2
        
        def prior(op1, op2):
            if op2 == "(" or op2 == ")":
                return False
            if (op1 == "*" or op1 == "/") and (op2 == "+" or op2 == "-"):
                return False
            return True
        
        i = 0
        nums, ops = [], []
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
                continue
            if c.isdigit():
                num = int(c)
                while i < len(s) - 1 and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                nums.append(num)
            elif c == "(":
                ops.append(c)
            elif c == ")":
                while ops[-1] != "(":
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()
            elif c in ["+", "-", "*", "/"]:
                while ops and prior(c, ops[-1]):
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.append(c)
            i += 1
        
        while ops:
            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
        
        return nums[0]