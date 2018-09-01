import unittest

class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """ 
        n = len(num)
        keep = n - k
        result = ""
        for c in num:
            while k > 0 and len(result) > 0 and result[-1] > c:
                result = result[:-1]
                k -= 1
            result += c
        
        return result[:keep].lstrip("0") or "0"
    
    def removeKdigitsTE1(self, num, k):
        def allNums(result, num, k):
            if num == "":
                result.append(0)
                return
            if k == 0:
                result.append(int(num))
                return
            else:
                for i in range(len(num)):
                    allNums(result, num[:i] + num[i + 1:], k - 1)
        
        result = []
        allNums(result, num, k)
        return str(min(result))

    def removeKdigitsTE2(self, num, k):
        if k == 0:
            return num
        
        minNum = int(num)
        while k > 0:
            minNumStr = str(minNum)
            n = len(minNumStr)
            for i in range(n):
                newNum = minNumStr[:i] + minNumStr[i + 1:]
                if newNum == "":
                    return "0"
                minNum = min(minNum, int(newNum))
            k -= 1
        return str(minNum)

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual("1219", target.removeKdigits("1432219", 3))
        self.assertEqual("0", target.removeKdigits("11", 2))
        self.assertEqual("0", target.removeKdigits("0", 0))        
        self.assertEqual("200", target.removeKdigits("10200", 1))
        self.assertEqual("0", target.removeKdigits("10", 2))
        self.assertEqual("0", target.removeKdigits("1234567890", 10))

if __name__ == '__main__':
    unittest.main()
        