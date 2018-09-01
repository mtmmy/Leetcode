import unittest

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign, num = 1, 0
        result = 0
        stackOp, stackNum = [], []

        for c in s.replace(" ", ""):
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                result += sign * num
                sign, num = 1, 0
            elif c == "-":
                result += sign * num
                sign, num = -1, 0
            elif c == "(":
                stackOp.append(sign)
                stackNum.append(result)
                sign, result = 1, 0
            elif c == ")":
                result = (result + sign * num) * stackOp.pop() + stackNum.pop()
                sign, num = 1, 0
        return result + sign * num


    def calculateSlow(self, s):
        """
        :type s: str
        :rtype: int
        """
        def realCalculate(s):
            s.reverse()
            while len(s) > 2:
                num1 = s.pop()
                oper = s.pop()
                num2 = s.pop()
                if oper == "+":
                    s.append(num1 + num2)
                elif oper == "-":
                    s.append(num1 - num2)
            return s[0]

        s, i, stack, leftParenses = s.replace(" ", ""), 0, [], []
        
        while i < len(s):
            if s[i] == ")":
                leftParen = leftParenses.pop()
                calFirst = stack[leftParen + 1:]
                stack = stack[:leftParen]
                stack.append(realCalculate(calFirst))
            if s[i] == "(":
                leftParenses.append(len(stack))
                stack.append(s[i])
            elif s[i].isdigit():
                num = ""
                while i < len(s) and s[i].isdigit():
                    if s[i].isdigit():
                        num += s[i]
                    i += 1
                stack.append(int(num))
                i -= 1
            elif s[i] == "+" or s[i] == "-":
                stack.append(s[i])
            i += 1
        return realCalculate(stack)

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(33, target.calculate("(1+(4+5+2)-3)+(6+18)"))
        self.assertEqual(2, target.calculate("  1 + 1  "))
        self.assertEqual(23, target.calculate("(1+(4+5+2)-3)+(6+8)"))        

if __name__ == '__main__':
    unittest.main()
        