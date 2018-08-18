class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        else:
            result = self.intToString(num)
            return result[1:]
        
    def intToString(self, n):
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        if n >= 1000000000:
            return self.intToString(n // 1000000000) + " Billion" + self.intToString(n % 1000000000)
        elif n >= 1000000:
            return self.intToString(n // 1000000) + " Million" + self.intToString(n % 1000000)
        elif n >= 1000:
            return self.intToString(n // 1000) + " Thousand" + self.intToString(n % 1000)
        elif n >= 100:
            return self.intToString(n // 100) + " Hundred" + self.intToString(n % 100)
        elif n >= 20:            
            return " " + tens[n // 10] + self.intToString(n % 10)
        elif n >= 1:
            return " " + digits[n]
        else:
            return ""