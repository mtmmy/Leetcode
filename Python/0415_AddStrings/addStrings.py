class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1
        result = ""
        carry = 0
        while i >= 0 or j >= 0:
            summa = 0
            if i >= 0 and j >= 0:
                summa = int(num1[i]) + int(num2[j]) + carry
                carry = summa // 10                
                summa = summa % 10
                i -= 1
                j -= 1
            elif i >= 0:
                summa = int(num1[i]) + carry
                carry = summa // 10
                summa = summa % 10
                i -= 1
            elif j >= 0:
                summa = int(num2[j]) + carry
                carry = summa // 10
                summa = summa % 10
                j -= 1
            result = str(summa) + result
        if carry != 0:
            result = "1" + result
        return result
                