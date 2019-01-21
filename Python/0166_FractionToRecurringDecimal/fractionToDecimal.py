class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == "0":
            return "NaN"
        
        result = ""
        
        if numerator / denominator < 0:
            result += "-"
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        result += str(numerator // denominator)
        numerator %= denominator
        if numerator != 0:
            result += "."
            
        i, dic = len(result), {}
        
        while numerator != 0:
            if numerator not in dic:
                dic[numerator] = i
            else:
                i = dic[numerator]
                result = result[:i] + "(" + result[i:] + ")"
                return result
            numerator *= 10
            result += str(numerator // denominator)
            numerator %= denominator
            i += 1
        return result

target = Solution()
target.fractionToDecimal(1, 7)