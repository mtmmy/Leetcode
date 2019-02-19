class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, sign, stack = 0, "+", []
        s = s.replace(" ", "")
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] *= num
                elif sign == "/":
                    if stack[-1] ^ num < 0 and stack[-1] % num != 0:                        
                        stack[-1] = stack[-1] // num + 1
                    else:
                        stack[-1] //= num
                sign = c                
                num = 0
                
        return sum(stack)
        
    def calculate2(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        i = 0
        
        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                stack.append(num)
                i = j
            elif s[i] == "+" or s[i] == "-":
                stack.append(s[i])
                i += 1
            elif s[i] == "*":
                num1 = stack.pop()
                j = i + 1
                num2 = ""
                while j < len(s) and (s[j].isdigit() or s[j] == " "):
                    if s[j] != " ":
                        num2 += s[j]
                    j += 1
                num2 = int(num2)
                stack.append(num1 * num2)
                i = j
            elif s[i] == "/":
                num1 = stack.pop()
                j = i + 1
                num2 = ""
                while j < len(s) and (s[j].isdigit() or s[j] == " "):
                    if s[j] != " ":
                        num2 += s[j]
                    j += 1
                num2 = int(num2)
                stack.append(num1 // num2)
                i = j
            elif s[i] == " ":
                i += 1
        
        
        if len(stack) != 1:
            result = 0
            i = 0
            while i < len(stack):
                if stack[i] == "+":
                    result = result + stack[i + 1]
                    i += 2
                elif stack[i] == "-":
                    result = result - stack[i + 1]
                    i += 2
                elif i == 0:
                    result = stack[i]
                    i += 1
                else:
                    i += 1
            return result
        
        return stack[0]
            