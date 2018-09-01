import unittest

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #return " ".join(s.split()[::-1])
        s = s.strip(" ")[::-1]
        i, j = 0, 0
        while i < len(s):
            while i < len(s) and s[i] != " ":
                i += 1
            s = s[:j] + s[j:i][::-1] + s[i:]

            j = i + 1
            while i < len(s) and s[i] == " ":
                i += 1
            
            s = s[:j] + s[i:]            
            i = j + 1

        return s
        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual("blue is sky the", target.reverseWords("  the   sky    is    blue  "))

if __name__ == '__main__':
    unittest.main()    
        