import unittest

class Solution:
    def validUtf8(self, data):
        count = 0
        for val in data:
            if count == 0:
                if val >> 3 == 30:
                    count = 3
                elif val >> 4 == 14:
                    count = 2
                elif val >> 5 == 6:
                    count = 1
                elif val >> 7 > 0:
                    return False
            else:
                if val >> 6 != 2:
                    return False
                count -= 1
        return count == 0

    def validUtf8_2(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return False

        i, n = 0, len(data)
        charType = 0
        while i < n:            
            if charType == 0:
                leadingBits = data[i] >> 3 & 31
                if leadingBits < 16:
                    charType = 0
                    i += 1                    
                elif leadingBits < 28:
                    charType = 2
                elif leadingBits < 30:
                    charType = 3
                elif leadingBits == 30:
                    charType = 4
                else:
                    return False                
            if charType > 0:                
                checkBytes = data[i + 1: i + charType]
                if len(checkBytes) < charType - 1:
                    return False
                j = 0
                while j < len(checkBytes):
                    nBits = checkBytes[j] >> 6
                    if nBits != 2:
                        return False
                    j += 1
                charType = 0
                i += j + 1
        return True

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual(True, target.validUtf8([232,174,169]))
        self.assertEqual(False, target.validUtf8([247]))
        self.assertEqual(True, target.validUtf8([247, 183, 182, 181, 1]))
        self.assertEqual(False, target.validUtf8([255]))
        self.assertEqual(False, target.validUtf8([145]))
        self.assertEqual(True, target.validUtf8([197,130,1,1,1,1,1,1,1]))
        self.assertEqual(True, target.validUtf8([197, 130, 1]))
        self.assertEqual(False, target.validUtf8([235, 140, 4]))

if __name__ == '__main__':
    unittest.main()
        