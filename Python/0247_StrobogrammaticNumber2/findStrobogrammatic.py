class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """        
        return self.fillup(n, n)
    
    def fillup(self, remainLen, length):
        if remainLen == 0:
            return [""]
        elif remainLen == 1:
            return ["0", "1", "8"]
        else:
            result = []
            subArrays = self.fillup(remainLen - 2, length)
            
            for a in subArrays:
                if remainLen != length:
                    result.append("0" + a + "0")
                result.append("1" + a + "1")
                result.append("6" + a + "9")
                result.append("8" + a + "8")
                result.append("9" + a + "6")
            return result
