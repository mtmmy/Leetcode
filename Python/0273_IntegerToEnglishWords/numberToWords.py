class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        else:
            digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            
            def intToString(n):        
                if n >= 1000000000:
                    return intToString(n // 1000000000) + " Billion" + intToString(n % 1000000000)
                elif n >= 1000000:
                    return intToString(n // 1000000) + " Million" + intToString(n % 1000000)
                elif n >= 1000:
                    return intToString(n // 1000) + " Thousand" + intToString(n % 1000)
                elif n >= 100:
                    return intToString(n // 100) + " Hundred" + intToString(n % 100)
                elif n >= 20:            
                    return " " + tens[n // 10] + intToString(n % 10)
                elif n >= 1:
                    return " " + digits[n]
                else:
                    return ""
            
            result = intToString(num)
            return result[1:]